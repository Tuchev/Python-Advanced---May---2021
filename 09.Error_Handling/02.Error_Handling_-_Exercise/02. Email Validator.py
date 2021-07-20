class EmailValidationError(Exception):
    pass


class NameNotFound(EmailValidationError):
    pass


class MustContainAtSymbol(EmailValidationError):
    pass


class TooManyAtSymbols(EmailValidationError):
    pass


class NameTooShortError(EmailValidationError):
    pass


class InvalidDomainError(EmailValidationError):
    pass


ALLOWED_DOMAINS = [".com", ".bg", ".org", ".net"]


def validate_email(email):
    if "@" not in email:
        raise MustContainAtSymbol("Email must contain @")

    username, domain, *rest = email.split("@")

    if len(rest) > 0:
        raise TooManyAtSymbols('the whole email must contain one and only one "@" symbol')
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if '.' + domain.split(".")[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {','.join(ALLOWED_DOMAINS)}")


def main():
    while True:
        email = input()
        if email == "End":
            break

        try:
            validate_email(email)
            print("Email is valid")
        except EmailValidationError as exception:
            print(exception)


if __name__ == "__main__":
    main()