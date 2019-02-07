from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from healthsite.core.forms import SignUpForm, AddExerciseForm
from healthsite.core.models import ExerciseData
from healthsite.core.models import TraineeTrainerData




@login_required
def profile(request):
    user_name = request.user.username
    userdata = User.objects.get(username=user_name)
    query_results = TraineeTrainerData.objects.all()
    return render(request, 'profile.html', {'query_results': query_results,
                                            'login_status': request.user.is_authenticated(),
                                            'username': request.user.username,
                                            'item': userdata
                                           })



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def contact(request):
    return render(request,'contact.html',{'content':['In case of any questions / suggestions, email me at:','niksysweety@tamu.edu'],
                                          'login_status': request.user.is_authenticated(),
                                          'username': request.user.username
                                          })


#def viewExercises(request):
 #   query_results = ExerciseData.objects.all()
   #  return render(request, 'viewExercises.html', {'query_results': query_results,
     #                                          'login_status': request.user.is_authenticated(),
    #                                           'username': request.user.username
      #                                         })


#def viewExercise(request):
 #   ExerciseName = request.GET.get('name')
  #  Exercise = ExerciseData.objects.get(Exercise_name=ExerciseName)
   # return render(request, 'viewExercise.html', {'item': Exercise,
    #                                          'login_status': request.user.is_authenticated(),
     #                                         'username': request.user.username
      #                                        })



@login_required
def addExercise(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            addExForm = AddExerciseForm(request.POST)
            if addExForm.is_valid():
                addExForm.save()
                #exercisename = addExForm.cleaned_data.get('exercise_name')
                return redirect('profile')
            else:
                addExForm = AddExerciseForm()
                return render(request, 'addExercise.html', {'form': addExForm,
                                                         'login_status': request.user.is_authenticated(),
                                                         'username': request.user.username
                                                         })
        else:
            addExForm = AddExerciseForm()
            return render(request, 'addExercise.html', {'form': addExForm,
                                                     'login_status': request.user.is_authenticated(),
                                                     'username': request.user.username
                                                     })
    else:
        return render(request,'login.html',
                      {'login_status': request.user.is_authenticated()
                      })



def viewExercises(request):
    query_results = ExerciseData.objects.all()
    return render(request, 'viewExercises.html', {'query_results': query_results,
                                               'login_status': request.user.is_authenticated(),
                                               'username': request.user.username
                                               })


def viewExercise(request):
    exName = request.GET.get('name')
    exercise = ExerciseData.objects.get(Exercise_name=exName)
    return render(request, 'viewExercise.html', {'item': exercise,
                                              'login_status': request.user.is_authenticated(),
                                              'username': request.user.username
                                              })

