Update the `User` model and all relevant code to add a string field named `name` to the model. This `name` field will be used to store the user's full name.

- Update the user model in `app/models.py`
- Run `alembic revision --autogenerate -m "Add name field to user"` to generate a migration
- Update `app/schemas/requests.py` and `app/schemas/responses.py` accordingly
- Update `app/api/endpoints/auth.py` accordingly as well.

I have added a failing assert in `app/tests/test_users/test_read_current_user.py` that verifies that the `read_current_user` route returns a `name` field. I have also updated the tests in `app/tests/test_auth/test_register_new_user.py` to pass in a `name` field to the `register_new_user` route. Make sure these tests pass.
