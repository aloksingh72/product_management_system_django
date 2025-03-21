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

# dashboard view 
def dashboard(request):
    if request.method == "POST":
        category_name = request.POST.get("category_name")
        print(category_name)
        admin_instance = Category()
        admin_instance.category_name = category_name
        admin_instance.save()

        return redirect("/admin-panel/dashboard")
    cat = Category.objects.all().order_by("-id")
    products = Product.objects.all().order_by("-id")
    categories = Category.objects.all() 
    
    return render(request,"adminhome.html",context={'category_data':cat,'product_data':products,})


def delete_cat(request, pk):
    delete_cat = Category.objects.filter(id = pk).last()
    delete_cat.delete()
    return redirect("/admin-panel/dashboard")






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

        # product model  instance 
        prod_instance = Product()
        
        prod_instance.prod_name = prod_name
        prod_instance.description = description
        prod_instance.price = price
        # prod_instance.image = image
        prod_instance.category_id = category
        prod_instance.save()
        print("================== Product Saved ==================")

        return redirect("/admin-panel/dashboard")
 

    return render(request,"adminhome.html")

def delete_prod(request,pk):
    delete_prod = Product.objects.filter(id = pk).last()
    delete_prod.delete()
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



# prod_name
def edit_prod(request,pk):
    edit_prod = Product.objects.filter(id = pk).last()
    category_data =  Category.objects.all()
    if request.method == "POST":
        new_product_name = request.POST.get("product_name")
        new_description = request.POST.get("description")
        new_price = request.POST.get("price")
        new_category_name = request.POST.get("category_name")
        print(new_category_name)

        if new_product_name or new_description or new_price or new_category_name:
            edit_prod.prod_name = new_product_name
            edit_prod.description = new_description
            edit_prod.price = new_price
            edit_prod.category_id = new_category_name
            edit_prod.save()
            return redirect("/admin-panel/dashboard")
    return render(request,"editprod.html", {"category_data": category_data,"edit_prod":edit_prod})

