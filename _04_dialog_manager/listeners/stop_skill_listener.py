from _04_dialog_manager.event import subscribe
from decouple import config
from voice_assistant_helper import write_to_file

def handle_stop_event(slots = None):
    """
    writes empty output to file
    @param slots: empty placeholder
    """
    write_to_file(file_path = config('DIALOG_MANAGER_OUTPUT_PATH'), text = "")

def setup_stop_event_handlers():
    """
    subcribes all events 
    """
    subscribe("stop", handle_stop_event)
