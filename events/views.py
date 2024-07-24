from django.shortcuts import render,redirect
from .form import CreateEventForm,EventAdminResponseForm
from .models import Event
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

#create event
@login_required
def create_event_proposal(request):
    if request.method =='POST':
        form = CreateEventForm(request.POST)
        if form.is_valid():
            var =form.save(commit=False)
            var.user = request.user
            var.save()
            messages.success(request,'Event proposal submitted successfully and is under review.')
            return redirect('home')
        else:
            messages.warning(request,'Oops,something went wrong!')
            return redirect('create-event-proposal')
    else:
        form = CreateEventForm()
        return render(request,'event/create-event-proposal.html',{'form':form})

#view all events proposals
@login_required
def all_event_proposals(request):
    events = Event.objects.filter(user = request.user)
    return render(request,'event/all-event-proposals.html',{'events':events})

#event proposal queue (for admin)
@login_required
def event_proposal_queue(request):
    events = Event.objects.filter(status = 'Pending')
    return render(request,'event/event-proposal-queue.html',{'events':events})

#approve/decline event proposals (for admin)
def admin_response(request,pk):
    event = Event.objects.get(pk=pk)
    if request.method =='POST':
        form = EventAdminResponseForm(request.POST,instance=event)
        if form.is_valid():
            var = form.save()
            if var.status == 'Approve':
                messages.success(request, f'You have approved the event proposal for {var.user}')
                return redirect('event-proposal-queue')
            elif var.status == 'Decline':
                messages.success(request,f'You have declined the event proposal for {var.user}')
                return redirect('event-proposal-queue')
            else:
                return redirect('home')
        else:
            messages.warning(request,'Oops,something went wrong.')
            return redirect('home')
    else:
        form = EventAdminResponseForm(instance=event)
        return render(request,'event/admin-response.html',{'form':form,'event':event})

            