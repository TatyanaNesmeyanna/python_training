# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="FirstName", middlename="Middlename", lastname="Lastname", nickname="Nickname", title="Title", company="Company", address="Address", home="1",
                               mobile_phone="777777", work_phone="666666", fax="555555", email="test@mail.ru", address2="test adress", phone2="1", notes="no"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                             mobile_phone="", work_phone="", fax="", email="", address2="", phone2="", notes=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

