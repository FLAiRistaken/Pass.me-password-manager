import pytest
import pytest_mock
from package import authenitcation

def test_authentication(mocker):
    email = "test@test.com"
    password = "Password123"
    
    # mocks the return from dbConnect.queryone, used in @authenitcation.authentication,
    # which typically returns the password hash associated with the given email address,
    # as the hash for the password "Password123"
    mocker.patch(
        'package.db_connect.dbConnect.queryone',
        return_value=["$argon2id$v=19$m=65536,t=3,p=4$cmh19ZsYNrzqYMchSidPkg$pHozP9eMhpFknEy7cPYO35wjl1gGDQAK2xfLDry8OA0"]
    )
    expected = True
    actual = authenitcation.Authentication(email, password).authenticated
    assert expected == actual
    