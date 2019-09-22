# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="FirstName", middlename="Middlename", lastname="Lastname", nickname="Nickname", title="Title", company="Company", address="Address", home="1",
                               mobile_phone="777777", work_phone="666666", fax="555555", email="test@mail.ru", address2="test adress", phone2="1", notes="no")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                             mobile_phone="", work_phone="", fax="", email="", address2="", phone2="", notes="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
