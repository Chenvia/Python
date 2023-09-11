class Blocker():

    def __init__(self):

        self.telemetry = [
            'df.telemetry.microsoft.com',
            'oca.telemetry.microsoft.com',
            'oca.telemetry.microsoft.com.nsatc.net',
            'redir.metaservices.microsoft.com',
            'reports.wes.df.telemetry.microsoft.com',
            'services.wes.df.telemetry.microsoft.com',
            'settings-sandbox.data.microsoft.com',
            'settings-win.data.microsoft.com',
            'sqm.df.telemetry.microsoft.com',
            'sqm.telemetry.microsoft.com',
            'sqm.telemetry.microsoft.com.nsatc.net',
            'telecommand.telemetry.microsoft.com',
            'telecommand.telemetry.microsoft.com.nsatc.net',
            'telemetry.appex.bing.net',
            'telemetry.microsoft.com',
            'telemetry.urs.microsoft.com',
            'vortex-sandbox.data.microsoft.com',
            'vortex-win.data.microsoft.com',
            'vortex.data.microsoft.com',
            'watson.telemetry.microsoft.com',
            'watson.telemetry.microsoft.com.nsatc.net',
            'watson.ppe.telemetry.microsoft.com',
            'wes.df.telemetry.microsoft.com',
            'ca.telemetry.microsoft.com',
            'cache.datamart.windows.com',
            'diagnostics.support.microsoft.com'
        ]

        self.live = [
            'vortex-bn2.metron.live.com.nsatc.net',
            'vortex-cy2.metron.live.com.nsatc.net',
            'watson.live.com',
            'watson.microsoft.com',
            'feedback.search.microsoft.com',
            'feedback.windows.com',
            'corp.sts.microsoft.com,'
            'diagnostics.support.microsoft.com',
            'i1.services.social.microsoft.com',
            'i1.services.social.microsoft.com.nsatc.net',
            'vortex-bn2.metron.live.com.nsatc.net',
            'vortex-cy2.metron.live.com.nsatc.net'
            ]

        self.defender = [
            'spynet2.microsoft.com',
            'spynetalt.microsoft.com'
            ]

        self.ad = [
            'flashtalking.com',
            'adnxs.com',
            'c.msn.com',
            'g.msn.com',
            'h1.msn.com',
            'msedge.net',
            'rad.msn.com',
            'ads.msn.com',
            'adnexus.net',
            'ac3.msn.com',
            'c.atdmt.com',
            'm.adnxs.com',
            'rad.msn.com',
            'sO.2mdn.net',
            'ads1.msn.com',
            'ec.atdmt.com',
            'flex.msn.com',
            'rad.live.com',
            'ui.skype.com',
            'msftncsi.com',
            'a-msedge.net',
            'a.rad.msn.com',
            'b.rad.msn.com',
            'cdn.atdmt.com',
            'm.hotmail.com',
            'ads1.msads.net',
            'a.ads1.msn.com',
            'a.ads2.msn.com',
            'apps.skype.com',
            'b.ads1.msn.com',
            'view.atdmt.com',
            'watson.live.com',
            'preview.msn.com',
            'aidps.atdmt.com',
            'adnxs.com',
            'c.msn.com',
            'g.msn.com',
            'h1.msn.com',
            'msedge.net',
            'rad.msn.com',
            'ads.msn.com',
            'adnexus.net',
            'ac3.msn.com',
            'c.atdmt.com',
            'm.adnxs.com',
            'rad.msn.com',
            'sO.2mdn.net',
            'ads1.msn.com',
            'ec.atdmt.com',
            'flex.msn.com',
            'rad.live.com',
            'ui.skype.com',
            'msftncsi.com',
            'a-msedge.net',
            'a.rad.msn.com',
            'b.rad.msn.com',
            'cdn.atdmt.com',
            'm.hotmail.com',
            'ads1.msads.net',
            'a.ads1.msn.com',
            'a.ads2.msn.com',
            'apps.skype.com',
            'b.ads1.msn.com',
            'view.atdmt.com',
            'watson.live.com',
            'preview.msn.com',
            'aidps.atdmt.com',
            'preview.msn.com',
            'static.2mdn.net',
            'a.ads2.msads.net',
            'b.ads2.msads.net',
            'db3aqu.atdmt.com',
            'secure.adnxs.com',
            'www.msftncsi.com',
            'cs1.wpc.v0cdn.net',
            'live.rads.msn.com',
            'ad.doubleclick.net',
            'bs.serving-sys.com',
            'a-0001.a-msedge.net',
            'pricelist.skype.com',
            'a-0001.a-msedge.net',
            'a-0002.a-msedge.net',
            'a-0003.a-msedge.net',
            'a-0004.a-msedge.net',
            'a-0005.a-msedge.net',
            'a-0006.a-msedge.net',
            'a-0007.a-msedge.net',
            'a-0008.a-msedge.net',
            'a-0009.a-msedge.net',
            'preview.msn.com',
            'static.2mdn.net',
            'a.ads2.msads.net',
            'b.ads2.msads.net',
            'db3aqu.atdmt.com',
            'secure.adnxs.com',
            'www.msftncsi.com',
            'cs1.wpc.v0cdn.net',
            'live.rads.msn.com',
            'ad.doubleclick.net',
            'bs.serving-sys.com',
            'pricelist.skype.com',
            ]

    def build_header(self):

        return '\n\n# Entries below created by HostBlocker\n'
        

    def build_footer(self):

        return '# End of hostBlocker entries\n'
        
        
    def write_out(self, data):

        filename = r"C:\Windows\System32\Drivers\etc\hosts"

        with open(filename,'a') as debug_file:
            debug_file.write(data)
            debug_file.close()

    def build_entries(self, hosts, ip='0.0.0.0'):

        entries = ""

        for host in hosts:
            entries += ("%s %s\n" % (ip, host))

        print(entries)
        
        return entries


    def out_all(self):

        hosts = ""
        ARGS = [ self.build_header(),
                     self.build_entries(self.telemetry),
                     self.build_entries(self.live),
                     self.build_entries(self.defender),
                     self.build_entries(self.ad),
                     self.build_footer()
               ]
        
        for x in ARGS:
            hosts += x

        print(hosts) #Debugging

        self.write_out(hosts)

if __name__ == '__main__':
    block = Blocker()
    block.out_all()
