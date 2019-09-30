from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list" : [{
    	"restaurant_name": "Burger King",
    	"food_type": "Wooper!"}],
    	
    	"my_list" : [{
    	"restaurant_name": "Pappa Johns",
    	"food_type": "Pizza Pizza Pizza"}],
    	
    	"my_list" : [{
    	"restaurant_name": "Shawarma Restaurant",
    	"food_type": "Chicken Shawarma xD"}]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object":{"restaurant_name":"Burger king", "food_type":"Wooper!"}
    }

    
    return render(request, 'detail.html', context)
