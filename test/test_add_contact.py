from model.contact import Contact


def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(last_name='LastName', first_name='FirstName', address='Address', email='Email', phone='Phone'))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(last_name='', first_name='', address='', email='', phone=''))
    app.session.logout()
