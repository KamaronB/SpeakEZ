from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def pagination(request,data,num=10):
    paginator=Paginator(data,num)
    page=request.GET.get('page')

    try:
        items=paginator.page(page)
    except PageNotAnInteger:
        items= paginator.page(1)
    except EmptyPage:
         items=paginator.page(paginator.num_pages)
    #current page we're on
    index= items.number-1
    #max number of pages
    max_in= len(paginator.page_range)
    #pages to display at bottom e.g. <<page 5>>
    start_in = index - 5 if index>=5 else 0
    ##pages to display at bottom e.g. <<page 5>>
    end_in = index + 5 if index <= max_in-5 else max_in

    #page range
    page_range = paginator.page_range[start_in:end_in]

    return items,page_range
