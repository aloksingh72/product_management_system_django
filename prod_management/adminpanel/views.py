from django.shortcuts import render, redirect,get_object_or_404
from .models import *
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email)
        print(password)

        admin_instance = UserDetails.objects.filter(email =email).first()
        print(admin_instance)
        if admin_instance and admin_instance.password == password:
            print(admin_instance.id)
            if admin_instance.id ==1:
                return redirect("dashboard")
            else:
                return render(request,"userhome.html")
        else:
            return render(request,"login.html",{"error" :"Incorrect credential"})

    return render(request,"login.html")


def dashboard(request):
    if request.method == "POST":
        category_name = request.POST.get("category_name")
        print(category_name)
        admin_instance = Category()
        admin_instance.category_name = category_name
        admin_instance.save()

        return redirect("/admin-panel/dashboard")
    cat = Category.objects.all().order_by("-id")
    
    return render(request,"adminhome.html",context={'category_data':cat})


def delete_cat(request, pk):
    delete_cat = Category.objects.filter(id = pk).last()
    delete_cat.delete()
    return redirect("/admin-panel/dashboard")



def edit_cat(request, pk):
    # Fetch the specific category based on the primary key
    # edit_category = get_object_or_404(Category, id=pk)  
    edit_category =  Category.objects.filter(id=pk).last() 
    print(edit_category)

    if request.method == "POST":
        new_category_name = request.POST.get("category_name")  # Get updated value from form
        if new_category_name:
            edit_category.category_name = new_category_name  # Update category name
            edit_category.save()  # Save changes
            return redirect("/admin-panel/dashboard")  # Redirect to admin panel after saving

    # Render the editcat.html template and pass the category data
    return render(request, "editcat.html", {"edit_category": edit_category})



# add product features
def add_product(request):
    if request.method == "POST":
        prod_name = request.POST.get("prod_name")
        print(prod_name)
        description = request.POST.get("description")
        print(description)
        price = request.POST.get("price")
        print(price)
        # image = request.FILES.get("image")
        category = request.POST.get("category")
        print(category)

        prod_instance = Product()
        
        prod_instance.prod_name = prod_name
        prod_instance.description = description
        prod_instance.price = price
        # prod_instance.image = image
        prod_instance.category_id = category
        prod_instance.save()
        print("================== Product Saved ==================")

        return redirect("/admin-panel/dashboard")
    products = Product.objects.all().order_by("-id")
    categories = Category.objects.all() 
    print("Fetched Products:", products)  # Debugging
    print("Fetched Categories:", categories)

    return render(request,"adminhome.html",context = {'product_data':products,"category_data":categories})





