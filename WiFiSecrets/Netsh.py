class NetworkShell():

    """

    \Windows\WiFi\Secrets\

    Module returns all saved WiFi profiles and their corresponding keys.

    Levereges netsh(Network Shell) to list profiles and retrive key.

        Requires administrative access to launch 'netsh.exe'.

        Returns value in plain text.
        
    """

    def __init__(self):

        self.keys = []

        for x in self.list_profiles():
            keys = self.recover_key(x)
            self.keys.append("%s : %s " % (keys[0], keys[1]))


    def recover_key(self, profile):

        """
        Levereges netsh(Network Shell) to return a saved profiles network key.

        Requires Admin Access.
        """

        from re import compile as cmpile
        from re import findall
        
        CMD = r'C:\Windows\System32\netsh.exe wlan show profiles name="%s" key=clear' % profile 

        output = self.run_process(CMD)
        exp = cmpile("Key Content\s+:\s+(\S+)")

        return (profile, exp.findall(output)[0])

    def list_profiles(self):

        """
        Levereges netsh(Network Shell) to display saved WiFi profiles.

        Requires Admin Access.
        """

        from re import compile as cmpile
        from re import findall

        res = []
        CMD = r'C:\Windows\System32\netsh.exe wlan show profile'

        output = self.run_process(CMD)
        exp = cmpile(r"\s+:\s+\S+")

        for x in exp.findall(output):
            res.append(x.strip(' ').strip(': '))

        return res
        
    def run_process(self, cmd):

        """
        Uses Subprocess module to launch a command without a window.

        Returns the output of the comand.
        """

        from subprocess import check_output, STARTUPINFO, STARTF_USESHOWWINDOW

        start_up_info = STARTUPINFO()
        start_up_info.dwFlags |= STARTF_USESHOWWINDOW    
        output = check_output(cmd, startupinfo=start_up_info)

        return output

    def get_keys(self):

        return self.keys
