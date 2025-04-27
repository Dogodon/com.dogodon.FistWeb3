from django.views.generic import ListView

from calendarapp.models import Event


class AllEventsListView(ListView):
    """ All event list views """

    template_name = "calendarapp/events_list.html"
    model = Event
    ###################
    # context_object_name = "latest_events"  # 👈 Ajoute ceci

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_events"] = self.get_queryset()
        return context

    # def get_queryset(self):
    #     return Event.objects.get_all_events(user=self.request.user)
    def get_queryset(self):
        print("Vue appelée par :", self.request.user)
        return Event.objects.get_all_events(user=self.request.user)









class RunningEventsListView(ListView):
    """ Running events list view """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)

class UpcomingEventsListView(ListView):
    """ Upcoming events list view """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_upcoming_events(user=self.request.user)
    
class CompletedEventsListView(ListView):
    """ Completed events list view """

    template_name = "calendarapp/events_list.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_completed_events(user=self.request.user)
    


