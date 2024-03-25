function entryOpen(entryDate){
    let entDate = new Date(entryDate);entDate.setHours(0,0,0,0);
    let todayDate = new Date();todayDate.setHours(0,0,0,0);
    if(entDate > todayDate){
        alert("Can't make an entry for a future date.");
        return false;
    }
    window.location.href = `/dashboard/entry/${entryDate}`;
}

document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    dayHeaderFormat: { weekday: 'short' },
    headerToolbar: {
    start: 'title',
    center: '',
    end: 'today prev,next,dayGridMonth,multiMonthYear',
    },
    dayMaxEventRows: 1,
    dayHeaderClassNames: function(arg) {
        return ['custom-day-header'];
    },
    dateClick: function(info) {
      entryOpen(info.dateStr);
      
    },
    eventClick: function(info) {
      entryOpen(info.event.startStr);
    },
    viewDidMount: async function(view) {
      let view_title = view.view.title
      let date = view.view.currentStart; // Get the first date visible in the calendar view
      let view_list = view_title.split(" ");
      let date_data = ""
      if(view_list.length > 1){
        await addEvents(`${date.getFullYear()}-${date.getMonth()+1}`,calendar)
      }
      else{
        await addEvents(String(date.getFullYear()),calendar)
      }
    },
    });
  calendar.render();
});

async function addEvents(dates,calendar){
  let res = await getData(`/dashboard/api/list/entries/${dates}/`);
  resJson = await res.json();
  calendar.getEvents().forEach(function(event) {
    event.remove();
  });
  resJson.forEach(event => {
    calendar.addEvent({
      title: event['entry_title'],
      start: event['date'],
      allDay: true
    });
  });
}