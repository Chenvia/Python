import requests, json

#https://www.linode.com/docs/guides/configure-spf-and-dkim-in-postfix-on-debian-9/#key-rotation

class LinodeDomain():

    def __init__(self, API_KEY):

        self.headers = {
            "Authorization" : "Bearer %s" % API_KEY
            }


    def get_handler(self, url, payload=None):

        response = requests.get(url, headers=self.headers, data=payload)
        return json.loads(response.text.encode('utf-8'))


    def post_handler(self, url, payload=None):

        response = requests.request("POST", url, headers=self.headers, json=payload)
        return json.loads(response.text.encode('utf-8'))


    def delete_handler(self, url):
        response = requests.request("DELETE", url, headers=self.headers)
        return json.loads(response.text.encode('utf-8'))


    def get_domains(self):

        return self.get_handler("https://api.linode.com/v4/domains")


    def get_domain_id(self, domain_name):

        for domain in self.get_domains()['data']:
            if domain["domain"] == domain_name:
                return domain['id']
        return None


    def get_domain_records(self, domain_id=False, domain_name=False):

        if not domain_id and not domain_name:
            return False

        if domain_name:
            domain_id = self.get_domain_id(domain_name)

        if domain_id:
            return self.get_handler("https://api.linode.com/v4/domains/%s/records" % domain_id)
        else:
            return False


    def get_dkim_records(self, domain):

        results = []

        for record in self.get_domain_records(domain_name=domain)["data"]:
            if record["type"] == "TXT":
                try:
                    selector, extension = record["name"].split(".")
                    int(selector)
                    if extension == "_domainkey":
                        results.append((selector, record["target"], record['id']))
                                                
                except:
                    continue

        return results


    def set_domain_record(self, record_type, name, target, domain_id=False, domain_name=False):

        data = {
            "type" : record_type,
            "name" : name,
            "target" : target
            }

        if not domain_id and not domain_name:
            return False

        if domain_name:
            domain_id = self.get_domain_id(domain_name)

        if domain_id:
            return self.post_handler("https://api.linode.com/v4/domains/%s/records" % domain_id, payload=data)


    def delete_domain_record(self, domain_id, record_id):
        return self.delete_handler("https://api.linode.com/v4/domains/%s/records/%s" % (domain_id, record_id))


    def delete_old_dkim(self, domain_name):

        domain_id = self.get_domain_id(domain_name)

        records = self.get_dkim_records(domain_name)

        oldest_record = ""
        oldest_selector = "999999"

        for record in records:
            if int(record[0]) < int(oldest_selector):
                oldest_record = record
                oldest_selector = record[0]

        self.delete_domain_record(domain_id, oldest_record[2])


if __name__ == '__main__':

    worker = LinodeDomain("API_KEY_HERE")
    
    
