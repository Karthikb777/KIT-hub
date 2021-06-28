from django.shortcuts import render, redirect
from .models import Note, NotesOfUser, ModRequests
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from .filters import NoteFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import NoteForm, CreateUserForm, LoginForm, ModRequestForm
from .decorators import UnauthenticatedUser, is_moderator
from django.http import HttpResponse, FileResponse, Http404
from django.contrib.auth.decorators import login_required, user_passes_test

   
'''

    wrap the note upload and update form with a uk-card-hover div

    account details with the list of notes the user has uploaded - done
    page to ask for confirmation to delete a note - done(sort of)
    implement login with google - done
    build a landing page
    create a view to let users download notes files - done
    implement searchbox - done
    implement filtering( optional, will think about it )
    add a functionality to check if a username exists while registering a user, throw an error if the username exists 

    finish the moderator application page tomorrow by adding more details

    and also add the functionality to send an email when the application has been approved.

'''

def landingPage(request):
    return render(request, 'main/hi.html', {})

@login_required(login_url='login')
def homePage(request):
    
    # print(Site.objects.get(name='kitcclub.herokuapp.com').id)
    # print(get_current_site(request).name)
    # print(Group.objects.all())
    noteList = Note.objects.all()[::-1]
    context = {
        'note': noteList,
    } 
    # print(request.user.image.url)
    return render(request, 'main/homePage.html', context)
    
@login_required(login_url='login')
def noteDetails(request, name):
    # note = Note.objects.get(id=priKey)
    note = Note.objects.get(name=name)
    context = {
        'note': note,
    }
    return render(request, 'main/noteDetails.html', context)

@login_required(login_url='login')
def noteDownload(request, name):
    # first the note gets added to the user account as the history of downloads and then the file is sent to be downlaoded
    NotesOfUser.objects.update_or_create(User=request.user, note=Note.objects.get(name=name))
    # try:
    #     # if not NotesOfUser.objects.filter(User=request.user, note=Note.objects.get(name=name)):
    #     #     NotesOfUser.objects.create(User=request.user, note=Note.objects.get(name=name))
    #     print(request.user)
    # except:
    #     pass
    #     # return Http404
    note = Note.objects.get(name=name).file
    return FileResponse(note, as_attachment=True, filename=note.name)
    

# @is_moderator
@login_required(login_url='login')
def accDetails(request):
    downloads = NotesOfUser.objects.filter(User=request.user)[::-1]
    if request.user.groups.filter(name='Moderator').exists():
        details = Note.objects.filter(uploadedBy=request.user)[::-1]
    else:
        details = False
    print(details)
    context = {
        'details': details,
        'downloads': downloads,
    }

    return render( request, 'main/accDetails.html', context )


@UnauthenticatedUser
def signUp(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
        
        else:
            messages.error( request, "Something went wrong with the signup process. Please try again." )
    
    context = {
        'form': form,
    }
    return render( request, 'main/signUp.html', context )

    
@UnauthenticatedUser
def loginUser(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate( request, username = username, password = password )
            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.error(request, 'Username or password is incorrect!')

    context = {
        'form': form,
    }

    return render( request, 'main/login.html', context )

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def searchResults(request):
    searchRes = Note.objects.all()
    if request.method == 'POST':
        filter = NoteFilter( request.POST, queryset=searchRes )
        res = {
            'note': filter.qs,
            'name': filter.data['name'],
            'label': filter.data['label'],
            'user': filter.data['user'],
        }
        print(filter.data["user"])
        return render( request, 'main/searchRes.html', res )
    # print(request.GET)
    filter = NoteFilter( request.GET, queryset=searchRes )
    # build the search functionality here.
    context = {
        'filter': filter,
    }
    # print(filter.qs)
    return render( request, 'main/search.html', context )

@is_moderator
@login_required(login_url='login')
def noteUpload(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            # print(request.user)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            uploadedBy = request.user
            user = request.user.username
            file = form.cleaned_data['file']
            coverImage = form.cleaned_data['coverImage']
            impressions = 1
            label = form.cleaned_data['label']
            # form.save()
            Note.objects.create(name=name, description=description, uploadedBy=uploadedBy, impressions=impressions, label=label, file=file, coverImage=coverImage, user=user)
            return redirect('home')

        else:
            messages.error( request, 'something went wrong, please try again' )
    context = {
        'form': form,
    }
    return render(request, 'main/noteUploadUpdate.html', context)

@is_moderator
@login_required(login_url='login')
def updateNote(request, name, id):
    note = Note.objects.get(id=id, name=name, uploadedBy=request.user)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            print('hi')
            form.save()
            # updatedName = form.cleaned_data['name']
            # description = form.cleaned_data['description']
            # uploadedBy = request.user
            # file = form.cleaned_data['file']
            # coverImage = form.cleaned_data['coverImage']
            # impressions = 1
            # label = form.cleaned_data['label']
            # form.save()
            # Note.objects.get(name=name).update(name=updatedName, description=description, uploadedBy=uploadedBy, impressions=impressions, label=label, file=file, coverImage=coverImage)
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'main/noteUploadUpdate.html', context)

@is_moderator
@login_required(login_url='login')
def deleteNote(request, name, id):
    note = Note.objects.get(name=name, id=id)
    note.delete()
    return redirect('home')

@login_required(login_url='login')
def deleteNoteHistory(request, name):
    note = NotesOfUser.objects.get(User=request.user, note=Note.objects.get(name=name))
    note.delete()
    return redirect('home')

@login_required(login_url='login')
def modRequest(request):
    
    modReq = ModRequests.objects.filter(user=request.user).exists()
    applied = True if modReq else False
    
        # modReq = False
    form = ModRequestForm()
    if request.method == 'POST':
        form = ModRequestForm(request.POST)
        if form.is_valid():
            user = request.user
            description = form.cleaned_data['description']
            ModRequests.objects.create(user=user, description=description)
            return redirect('home')

    context = {
        'modrequest': form,
        'applied': applied,
    }

    return render( request, 'main/modrequest.html', context )

@login_required(login_url='login')
def about(request):
    return render( request, 'main/about.html', {} )

@login_required(login_url='login')
def approveModRequest(request, email):
    pass


@login_required(login_url='login')
def announcements(request):
    pass

#  this view will be for the announcements page
# build announcements model and build a model form
# view to add an announcement from a moderator account, edit an announcement, and deletion functionality


'''


views and things that should be done:

- homepage ( all the trending notes should be shown ) - done
- notes details page which contains the link to add the notes to the account - done
- view to upload the notes ( user must be logged in to upload notes ) - done
- view to download the notes - done
- account details - done
- login - done
- logout - done
- a searchbox to search for notes by name - done
- search result view - done
- landing page to introduce to the website
- also add sign in with google as the default auth protocol - done


'''