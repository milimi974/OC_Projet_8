from django.template.loader import render_to_string



def pagination(object, page_per_view=3):
    # create paginate view
    more = False
    min_page = 0
    max_page = 0

    page = object.number

    if object.paginator.num_pages < page_per_view:
        max_page = object.paginator.num_pages

    if object.paginator.num_pages > page_per_view:
        min_page = page - 2

        max_page = page + (page_per_view - 2)
        if min_page <= 0:
            min_page = 0
            max_page = max_page + 1

        if page == object.paginator.num_pages:
            min_page = page - page_per_view

        if max_page > object.paginator.num_pages:
            max_page = object.paginator.num_pages

        if max_page < object.paginator.num_pages:
            more = max_page + 1
            if more > object.paginator.num_pages:
                more = False
    context = {
        'total_page': range(min_page, max_page),
        'more': more,
        'paginate': object.paginator.num_pages > 0,
        'object': object
    }
    return render_to_string('partials/pagination.html', context)