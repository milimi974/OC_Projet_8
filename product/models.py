import os

import math
from django.db import models

# Create your models here.
from master.settings import BASE_DIR
from tools import upload_openfoodfact_cvs, upload_location, clear_string
import csv  # Manage cvs file

class Category(models.Model):
    """ Categories of product
        :argument
        model : parent

    """
    # fields
    name = models.CharField(max_length=255, unique=True)
    # var contain list of categories to save
    list = []
    # contain object instance
    list_object = {}

    def __str__(self):
        return self.name


    def extract(self, categories_str):
        """ extract categories name from list

            Keyword arguments:
            categories_str -- string of categories elements

        """
        b = self.str_to_list(categories_str)
        if b:
            # merge list and remove duplicate
            self.list = list(set().union(self.list, b))


    def str_to_list(self, strvar):
        """ Return a list of categories object

            Keyword arguments:
            strvar -- string of product elements

        """
        # test type of value if string
        if type(strvar) is str and strvar:
            # Make a list with string
            return [x.strip() for x in strvar.split(',')]
        return False


    def create_categories(self):
        # create categories list
        if self.list:
            for category in self.list:
                category_qs, create = Category.objects.get_or_create(name=category)
                # stock category object by name
                self.list_object[category] = category_qs

    def add_category_list(self, name):
        """add one element name to list
            Keyword arguments:
            name -- string name of category
        """
        # merge list and remove duplicate
        self.list = list(set().union(self.list, list(name)))

    def get_category(self, name):
        """ return category object by name
            :argument
            name : object name

        """
        try:
            self.list_object[name]
            return self.list_object[name]
        except:
            return False

    def reset(self):
        """ reset list """
        self.list = []
        self.list_object = {}


class Shop(models.Model):
    """ Shops of product
        :argument
        model : parent

    """
    # fields
    name = models.CharField(max_length=255, unique=True)

    # var contain list of categories to save
    list = []
    # contain object instance
    list_object = {}

    def __str__(self):
        return self.name

    def extract(self, shops_str):
        """ extract shops name from list

            Keyword arguments:
            shops_str -- string of shops elements

        """
        b = self.str_to_list(shops_str)
        if b:
            # merge list and remove duplicate
            self.list = list(set().union(self.list, b))

    def str_to_list(self, strvar):
        """ Return a list of shops object

            Keyword arguments:
            strvar -- string of product elements

        """
        # test type of value if string
        if type(strvar) is str and strvar:
            # Make a list with string
            return [x.strip() for x in strvar.split(',')]
        return False

    def create_shops(self):
        # create shops list
        if self.list:
            for shop in self.list:
                shop_qs, create = Shop.objects.get_or_create(name=shop)
                # stock shop object by name
                self.list_object[shop] = shop_qs

    def add_category_list(self, name):
        """add one element name to list
            Keyword arguments:
            name -- string name of shop
        """
        # merge list and remove duplicate
        self.list = list(set().union(self.list, list(name)))


    def reset(self):
        """ reset list """
        self.list = []
        self.list_object = {}

    def get_shop(self, name):
        """ return shop object by name
            :argument
            name : object name

        """
        try:
            self.list_object[name]
            return self.list_object[name]
        except:
            return False


class ManageDB(models.Manager):

    # object for create all categories or shops
    categories = Category()
    shops = Shop()
    # list of product to save
    products = []


    # update database with data from OpenFoodFact API
    def update_db(self, qty=500, upload=True):
        if upload :
            upload_openfoodfact_cvs()

        # total entry save
        entry = -1
        loop = 1
        if qty > 500:
            loop = math.floor(qty / 500)
            qty = 500

        # Read Csv file from url
        filename = os.path.join(BASE_DIR, 'product/uploads/food.csv')
        with open(filename, newline='', encoding='utf-8') as csvfile:
            # Associating header with value in a dictionary
            reader = csv.DictReader(csvfile, delimiter='\t')
            if qty == -1:
                qty = sum(1 for row in reader)

            # Max line to save
            save_qty = 0


            # Start loop to read each line
            for row in reader:
                # Create a list of food object for each line
                if row['product_name'] and row['code']:
                    # format product
                    self.add_product_list({
                        'codebar': str(row['code']),
                        'link': row['url'],
                        'name': clear_string(row['product_name']),
                        'description': row['ingredients_text'],
                        'nutri_code': row['nutrition_grade_fr'],
                        'picture': row['image_url'],
                        'categories': self.categories.str_to_list(row['categories_fr']),
                        'shops': self.shops.str_to_list(row['stores']),
                    })

                    # add categories to object
                    self.categories.extract(row['categories_fr'])
                    # add shops to object
                    self.shops.extract(row['stores'])
                    save_qty += 1
                    entry += 1
                    if loop > 0 and save_qty > qty+1:
                        # create all categories
                        self.categories.create_categories()

                        # create all shops
                        self.shops.create_shops()

                        # create all product
                        self.create_products()
                        # reset data
                        save_qty = 0
                        loop -= 1
                        self.reset_components()

                    if loop == 0:
                        break

            if qty < 500:
                # create all categories
                self.categories.create_categories()

                # create all shops
                self.shops.create_shops()

                # create all product
                self.create_products()
            return 'Total entry : '+ str(entry)

    def reset_components(self):
        # reset all components
        self.categories.reset()
        self.shops.reset()
        self.products = []

    def create_products(self):
        """ method create a list of product
            do before create_products():
            self.add_product_list()

            # add on by one entry
            self.categories.add_category_list()
            self.shops.add_shop_list()

            # create all categories / shops
            self.categories.create_categories()
            self.shops.create_shops()

        :return:
        """
        # create all product
        for p in self.products:

            # check if product exist in DB
            # product_qs = Product.objects.filter()
            product = dict(p)

            categories = product.get('categories')
            shops =  product.get('shops')
            del product['categories']
            del product['shops']

            product_qs, created = Product.objects.update_or_create(
                codebar=product.get('codebar'),
                defaults=product,
            )

            self.add_product_categories(product_qs, categories)
            self.add_product_shops(product_qs, shops)

    def add_product_list(self, params):
        """add one element product  to list
           Keyword arguments:
           params -- dict key : name field, value : value of field
        """
        self.products.append(params)

    def add_product_categories(self, product, categories):
        """ add all product categories
            Keyword argument:
            product : qs product object
            categories : list category name
        """
        if categories:
            # list for bulk add
            objs = []
            # add product category
            for category in categories:
                category_qs = self.categories.get_category(category)
                if category_qs:
                    # if category exist test if relation already exist
                    qs = product.categories.filter(pk=category_qs.id)
                    if not qs.exists():
                        # if no relation add to list for bulk
                        objs.append(category_qs)
            if objs:
                # bulk add categories
                product.categories.add(*objs)

    def add_product_shops(self, product, shops):
        """ add all product shops
           Keyword argument:
           product : qs product object
           shops : list shop name
        """
        if shops :
            # list for bulk add
            objs = []
            # add product shop
            for shop in shops:
                shop_qs = self.shops.get_shop(shop)
                if shop_qs:
                    # if shop exist test if relation already exist
                    qs = product.shops.filter(pk=shop_qs.id)
                    if not qs.exists():
                        # if no relation add to list for bulk
                        objs.append(shop_qs)
            if objs:
                # bulk add shop
                product.shops.add(*objs)


class Product(models.Model):
    """ Product class
        :argument
        model : parent

    """

    # fields
    codebar = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    nutri_code = models.CharField(max_length=1)
    link = models.CharField(max_length=255)
    picture = models.URLField(max_length=255)
    image = models.ImageField(upload_to=upload_location,
                                null=True,
                                blank=True,
                                width_field="width_field",
                                height_field="height_field",
                                )
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)
    shops = models.ManyToManyField(Shop, related_name='products', blank=True)

    objects = ManageDB()


    def __str__(self):
        return self.name

