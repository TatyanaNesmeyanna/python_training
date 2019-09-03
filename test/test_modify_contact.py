# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_delete_contact"))
    app.contact.modify_first_contact(Contact(first_name="modified_name", middlename="", lastname="", nickname="", title="", company="", address="", home="",
                               mobile_phone="", work_phone="", fax="", email="", address2="", phone2="", notes=""))

def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_delete_contact"))
    app.contact.modify_first_contact(Contact(first_name="second_modified_name"))


def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name = "test_delete_contact"))
    app.contact.modify_first_contact(Contact(email="second_modified_email"))