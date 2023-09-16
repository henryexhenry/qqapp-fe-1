import datetime

from service.swagger_client.models.class_session import ClassSession

CALENDAR_MODE = (
    "timegrid",
    "daygrid",
    # "timeline",
    # "resource-daygrid",
    # "resource-timegrid",
    # "resource-timeline",
    "list",
    "multimonth",
)


def classs2event4timegrid(clsss:ClassSession):
    return {
        "id": clsss.id,
        "title": clsss.course.course_name,
        "lessons": clsss.lessons,
        "course_id": clsss.course.id,
        "class_length": clsss.course.class_length,
        "color": clsss.course.color,
        "comment": clsss.comment,
        "start": clsss.start_time.isoformat(),
        "end": clsss.end_time.isoformat(),
        "session_status": clsss.status,
        "backgroundColor": "grey" if clsss.status == 0 else clsss.course.color,
        "resourceId": "a",
        "display": "auto",
        "overlap": False
    }

def classs2event4daygrid(clsss:ClassSession):
    return {
        "id": clsss.id,
        "title": clsss.course.course_name,
        "lessons": clsss.lessons,
        "course_id": clsss.course.id,
        "class_length": clsss.course.class_length,
        "color": clsss.course.color,
        "comment": clsss.comment,
        "start": clsss.start_time.isoformat(),
        "end": clsss.end_time.isoformat(),
        "session_status": clsss.status,
        # "backgroundColor": clsss.course.color,
        "resourceId": "a",
        "display": "block" if clsss.status == 0 else "list-item",
        "overlap": False
    }


def build_option(mode, calendar_resources=None):
    today = datetime.date.today()
    last_sunday = (today - datetime.timedelta(days=today.weekday())).strftime("%Y-%m-%d")
    initial_date = last_sunday

    calendar_options = {
        "height": 1000,
        "eventOverlap": False,
        "eventDurationEditable": False,
        "themeSystem": "bootstrap5",
        "editable": True,
        "navLinks": True,
        "resources": calendar_resources,
    }

    if "resource" in mode:
        if mode == "resource-daygrid":
            calendar_options = {
                **calendar_options,
                "initialDate": initial_date,
                "initialView": "resourceDayGridDay",
                "resourceGroupField": "building",
            }
        elif mode == "resource-timeline":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
                },
                "initialDate": initial_date,
                "initialView": "resourceTimelineDay",
                "resourceGroupField": "building",
            }
        elif mode == "resource-timegrid":
            calendar_options = {
                **calendar_options,
                "initialDate": initial_date,
                "initialView": "resourceTimeGridDay",
                "resourceGroupField": "building",
            }
    else:
        if mode == "daygrid":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "dayGridDay,dayGridWeek,dayGridMonth",
                },
                "initialDate": initial_date,
                "initialView": "dayGridMonth",
            }
        elif mode == "timegrid":
            calendar_options = {
                **calendar_options,
                "initialView": "timeGridWeek",
                "slotMinTime": "06:00:00",
                "slotMaxTime": "24:00:00",
                "slotDuration": '00:30:00',
                "snapDuration": '00:05:00',
                "slotLabelInterval": "01:00",
            }
        elif mode == "timeline":
            calendar_options = {
                **calendar_options,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "timelineDay,timelineWeek,timelineMonth",
                },
                "initialDate": initial_date,
                "initialView": "timelineMonth",
            }
        elif mode == "list":
            calendar_options = {
                **calendar_options,
                "initialDate": initial_date,
                "initialView": "listMonth",
            }
        elif mode == "multimonth":
            calendar_options = {
                **calendar_options,
                "initialView": "multiMonthYear",
            }
    return calendar_options




events = [
    {
        "id": 7,
        "title": "Event 7",
        "color": "#FF4B4B",
        "start": "2023-09-01T08:30:00",
        "end": "2023-09-01T10:30:00",
        "resourceId": "a",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 8,
        "title": "Event 8",
        "color": "#3D9DF3",
        "start": "2023-09-01T07:30:00",
        "end": "2023-09-01T10:30:00",
        "resourceId": "b",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 9,
        "title": "Event 9",
        "color": "#3DD56D",
        "start": "2023-09-02T10:40:00",
        "end": "2023-09-02T12:30:00",
        "resourceId": "c",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 10,
        "title": "Event 10",
        "color": "#FF4B4B",
        "start": "2023-09-15T08:30:00",
        "end": "2023-09-15T10:30:00",
        "resourceId": "d",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 11,
        "title": "Event 11",
        "color": "#3DD56D",
        "start": "2023-09-15T07:30:00",
        "end": "2023-09-15T10:30:00",
        "resourceId": "e",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 12,
        "title": "Event 12",
        "color": "#3D9DF3",
        "start": "2023-09-21T10:40:00",
        "end": "2023-09-21T12:30:00",
        "resourceId": "f",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 13,
        "title": "Event 13",
        "color": "#FF4B4B",
        "start": "2023-09-17T08:30:00",
        "end": "2023-09-17T10:30:00",
        "resourceId": "a",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 14,
        "title": "Event 14",
        "color": "#3D9DF3",
        "start": "2023-09-17T09:30:00",
        "end": "2023-09-17T11:30:00",
        "resourceId": "b",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 15,
        "title": "Event 15",
        "color": "#3DD56D",
        "start": "2023-09-17T10:30:00",
        "end": "2023-09-17T12:30:00",
        "resourceId": "c",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 16,
        "title": "Event 16",
        "color": "#FF6C6C",
        "start": "2023-09-17T13:30:00",
        "end": "2023-09-17T14:30:00",
        "resourceId": "d",
        "display": "auto",
        "overlap": False
    },
    {
        "id": 17,
        "title": "Event 17",
        "color": "#FFBD45",
        "start": "2023-09-17T15:30:00",
        "end": "2023-09-17T16:30:00",
        "resourceId": "e",
        "display": "auto",
        "overlap": False
    },
]


calendar_resources = [
    {"id": "a", "building": "Building A", "title": "Room A"},
    {"id": "b", "building": "Building A", "title": "Room B"},
    {"id": "c", "building": "Building B", "title": "Room C"},
    {"id": "d", "building": "Building B", "title": "Room D"},
    {"id": "e", "building": "Building C", "title": "Room E"},
    {"id": "f", "building": "Building C", "title": "Room F"},
]