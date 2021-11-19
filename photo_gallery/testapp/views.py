from django.shortcuts import render
from testapp.models import Category,Photo
from testapp.forms import PhotoForm
from django.shortcuts import redirect
# Create your views here.

def HomeView (request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    photo_list = []
    for i in categories :
        for j in photos:
            if str(j.category).lower() == str(i).lower():
                photo_list.append(j)
                break

    # print("cat length :",len(categories))
    # print("pot length :",len(photo_list))
    # print("pot  :",photo_list[0])

    return render (request,'testapp/home.html',{'categories':categories,'photo_list':photo_list})


def PhotoListView (request,c):

    # photos = Photo.objects.filter(category=c)
    photos = Photo.objects.all()
    photo_list = []
    for j in photos:
        if str(j.category).lower() == c.lower():
            photo_list.append(j)

    print("category :",c)
    print("Photos :",photo_list)
    return render (request,'testapp/photo_list.html',{'photo_list':photo_list})



def PhotoView(request,id):
    photo = Photo.objects.get(id=id)
    return render (request,'testapp/photo.html',{'photo':photo})



def galleryView(request):
    photos = Photo.objects.all()
    print ("total photos, ",len(photos))
    return render (request,'testapp/gallery.html',{'photos':photos})



def AddPhotoView (request):


    if request.method == 'POST':
        cat = request.POST['newcat']
        print ("new_cat :",cat)


        if cat == "" :
            print ("new cat is empty")
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect ('gallery')
        else :
            c = Category.objects.create (name = cat)

            p = Photo.objects.create(category = c,image =  request.FILES.get('image'),desc = request.POST['desc'])

            return redirect ('gallery')

    else :

        form = PhotoForm()
        # print(form)

    return render (request,'testapp/add_photo.html',{'form':form})
