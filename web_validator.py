import re

class WebValidator:
    @staticmethod
    def validate_email(email):
        """
        Validate an email address using regex.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def check_domain(domain):
        """
        Check if a domain name is valid.
        """
        domain_regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$'
        return re.match(domain_regex, domain) is not None

# Example usage
if __name__ == '__main__':
    emails = ['example@mail.com', 'invalid-email.com']
    domains = ['example.com', '-invalid.com']

    for email in emails:
        print(f'Email: {email}, Valid: {WebValidator.validate_email(email)}')

    for domain in domains:
        print(f'Domain: {domain}, Valid: {WebValidator.check_domain(domain)}')