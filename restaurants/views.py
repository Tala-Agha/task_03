from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list":[
            {"restaurant_name":"pizza alrais","food_type":"Flavors of Italy & Lebanon"},
            {"restaurant_name":"Taqueria","food_type":"Mexican"},
            {"restaurant_name":"Pow Burger","food_type":"Burgers"},]}
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": {
    "restaurant_name":"pow burger",
    "food_type":"burgers"
    }

    }
    return render(request, 'detail.html', context)
