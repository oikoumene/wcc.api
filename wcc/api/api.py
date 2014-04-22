# -*- coding: utf-8 -*-

from plone.jsonapi.routes import add_plone_route

# CRUD
from plone.jsonapi.routes.api import get_items
from plone.jsonapi.routes.api import create_items
from plone.jsonapi.routes.api import update_items
from plone.jsonapi.routes.api import delete_items

from plone.jsonapi.routes.api import url_for


# GET
@add_plone_route("/wccdocument", "wccdocument", methods=["GET"])
@add_plone_route("/wccdocument/<string:uid>", "wccdocument", methods=["GET"])
def get(context, request, uid=None):
    """ get wccdocument
    """
    items = get_items("wcc.document.document", request, uid=uid, endpoint="wccdocument")
    return {
        "url": url_for("wccdocument"),
        "count": len(items),
        "items": items,
    }


# CREATE
@add_plone_route("/wccdocument/create", "wccdocument_create", methods=["POST"])
@add_plone_route("/wccdocument/create/<string:uid>", "wccdocument_create", methods=["POST"])
def create(context, request, uid=None):
    """ create wccdocument
    """
    items = create_items("wcc.document.document", request, uid=uid, endpoint="wccdocument")
    return {
        "url": url_for("wccdocument_create"),
        "count": len(items),
        "items": items,
    }


# UPDATE
@add_plone_route("/wccdocument/update", "wccdocument_update", methods=["POST"])
@add_plone_route("/wccdocument/update/<string:uid>", "wccdocument_update", methods=["POST"])
def update(context, request, uid=None):
    """ update wccdocument
    """
    items = update_items("wcc.document.document", request, uid=uid, endpoint="wccdocument")
    return {
        "url": url_for("wccdocument_update"),
        "count": len(items),
        "items": items,
    }


# DELETE
@add_plone_route("/wccdocument/delete", "wccdocument_delete", methods=["POST"])
@add_plone_route("/wccdocument/delete/<string:uid>", "wccdocument_delete", methods=["POST"])
def delete(context, request, uid=None):
    """ delete wccdocument
    """
    items = delete_items("wcc.document.document", request, uid=uid, endpoint="wccdocument")
    return {
        "url": url_for("wccdocument_delete"),
        "count": len(items),
        "items": items,
    }

# vim: set ft=python ts=4 sw=4 expandtab :
