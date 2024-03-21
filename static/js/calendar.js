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
    dayHeaderClassNames: function(arg) {
        return ['custom-day-header'];
    },
    dateClick: function(info) {
        entryOpen(info.dateStr);
    },
    });
    
    
  calendar.render();
});
