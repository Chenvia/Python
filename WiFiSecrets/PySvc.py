from win32serviceutil import ServiceFramework
  
class PySvc(ServiceFramework):

    """

    A superclass that handles the registering of code as a Windows service.

        Overwrite the main method with desired service code.

        Important fielda:

            _svc_name_ - NET START/STOP the service by the following name.
            _svc_display_name_ - Display name in Service Control Manager (SCM).
            _svc_description_ - Descriptive text within Service Control Manager (SCM).

    To Do:

        Add uninstall function to remove service.
    
    """
    
    _svc_name_ = "PySvc"
    _svc_display_name_ = "Python Test Service"
    _svc_description_ = "This service writes stuff to a file"  
      
    def __init__(self, args):

        """
        Uses win32event.CreateEvent to register a waitable event,

            allows to run code upon a STOP signal.
        """

        from socket import setdefaulttimeout
        from win32event import CreateEvent
        
        ServiceFramework.__init__(self,args)
        self.hWaitStop = CreateEvent(None, 0, 0, None)
        setdefaulttimeout(60)
      
    def SvcDoRun(self):
        
        """
        This function is called when the service is started.

            Registers an event in the Event Log.

            Calls main function.
        """

        from servicemanager import LogMsg, EVENTLOG_INFORMATION_TYPE, PYS_SERVICE_STARTED

        LogMsg(EVENTLOG_INFORMATION_TYPE, PYS_SERVICE_STARTED, (self._svc_name_,''))        
        self.main()

    def main(self):

        """

        """

        from win32event import WAIT_OBJECT_0, WaitForSingleObject

        with open('C:\\test.dat', 'w+')  as log_file:

            rc = None  
              
            # if the stop event hasn't been fired keep looping  
            while rc != WAIT_OBJECT_0:  
                log_file.write('TEST DATA\n')  
                log_file.flush()  
                # block for 5 seconds and listen for a stop event  
                rc = WaitForSingleObject(self.hWaitStop, 5000)  
                  
            log_file.write('SHUTTING DOWN\n')  
            log_file.close()
         
    def SvcStop(self):

        """
        This function is called when the service is being shut down.

            Leverages ReportServiceStatus to signal shutdown to SCM.
        """

        from win32service import SERVICE_STOP_PENDING
        from win32event import SetEvent     
        
        self.ReportServiceStatus(SERVICE_STOP_PENDING)  
        SetEvent(self.hWaitStop)  
          
if __name__ == '__main__':

    from win32serviceutil import HandleCommandLine

    HandleCommandLine(PySvc) 
