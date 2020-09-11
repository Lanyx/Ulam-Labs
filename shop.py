# pdoc --html --force shop.py

""" # Recruitment task for Ulam Labs (Wrocław, Poland) prepared by Grzegorz Wochlik
    wochlik.gm@gmail.com
-----
Dummy program concentrating on design and documentation of the API end points.

I ran into some irony. I was trying to get a professional look to the
documentation, rather than the cut-and-paste text file output. I looked for some
tools like 'sphinx' and 'mkdoc'. The irony is that tools to aid with
documentation were so poorly documented that they were unusable. Also, they
didn't do their job properly.

Then, I found a gem named 'pdoc'. (I like the Ruby language, hence the
reference). This tool is no fuss, no nonsense. The single example gets right to
the point. The additional parameter ('--force') was easy to find. It overwrites
the current HTML file.

Pass or fail, as ususal, I made a {mountain from a molehill}*; this project was
an interesting experience. It opened my eyes to an alternative career path as a
"Software Architect" (I thank You for that). Effectively, my little bit of
knowledge about everything becomes useful. Additionally, this experience has
re-affirmed my values: preference to morning work instead of evening,
constant editing to make sure it is perfect, constant stopping to think 'is
this correct?', the testing after every paragraph. The grand final, the grand
discovery: I still can't fit into a time budget.

As you can clearly see, I also have a passion for writing. Well, here I am
{opening a can of worms}*. Anyway, I'll need to move onto technical matters.

{}* = Idiom in english
"""

#-------------------------------------------------------------------------------
def list_products(dBriefcase):
    """Returns information about items available for purchase in the shop.

    Method looks through the database based on the search and indexing
    parameters provided. A structure is then returned. Note that error handling
    is incoperated into the response.

    Parameters
    ----------
        dBriefcase (dictionary)
        This is an all-in-one container for transporting variables into the
        method. The keys required are listed below:

            dBriefcase["iIdx"] (integer)
                Index to the paginated data. It is used to break up a long
                list into smaller pieces. For example, if there are 314 items
                for a particular keyword, the caller may want to fetch in
                batches of 5. 'iIdx' will be set to 0 for the first batch and
                to 4 for the second, and so on.

            dBriefcase["iMax_res"] (integer)
                Maximum number of results in this output.

            dBriefcase["sItem_filter"] (string, none)
                (string) datatype:
                    Keyword for searching the 'description' fields of products
                (none) datatype:
                    Show all products.

    Returns - Valid data
    -------
    A dictionary is returned containing key-value pairs. However, the structure
    for valid data is different from error notification. The 'sStatus' key is
    common to both 'valid data' and 'error' returns. It determines the further
    structure of the response

    dOutput (dictionary)

        dOutput["sStatus"] = "OK"
            The string "OK" is returned under the "sStatus" key, to indicate
            that non-error data is available.

        dOutput["iIdx_n"] (integer)
            Actual index, within the specified search, to the last item
            returned. If incremented, it can be used as the 'dBriefcase["idx"]'
            input in the next search to retrieve the next batch of items.

        dOutput["iSearch_tot"] (integer)
            Total number of items in the search

        dOutput["aItems"] (list of dictionaries)
            Information about items requested. Each item in the list has the
            following structure. The 'n' (integer) in the structure indexes the
            item number on the list

            dOutput["aItems"][n]["sItem_id"] (string)
                Unique item identifier as a string. May be a sequential
                alpha-numeric code.

            dOutput["aItems"][n]["sBrand"] (string)
                Manufacturer name.

            dOutput["aItems"][n]["sDesc"] (string)
                Searchable item description

            dOutput["aItems"][n]["sSize"] (string)
                If items are available in varous sizes (for example clothing,
                TV's) then a string is specifed.
                If the item is a 'one-size-fits-all', then the string 'N/A'
                is used ('Not applicable')

                So, "blue jeans size 38" will have a seperate entry to "blue
                jeans size 36". Also "black jeans size 38" will also be
                seperate.

            dOutput["aItems"][n]["sColour"] (string)
                Main colour or pattern of the item.

                So, "blue jeans size 38" will have a seperate entry to "black
                jeans size 38". Also "blue jeans size 38" will also be
                seperate.

            dOutput["aItems"][n]["fPrice"] (float)
                Price of the item in the "sCurrency" (see below) units.

            dOutput["aItems"][n]["sCurrency"] (string)
                ISO-4217 currency code, in which the item is priced. For
                example, the Polish Zloty has the code "PLN". The string "PLN"
                would be entered in this field

            dOutput["aItems"][n]["iStock"] (integer)
                How many items are currently available for purchase.

            dOutput["aItems"][n]["aPhotos"] (list of strings)
                Links to photos of the item

    Returns -- Error output
    -------
    A dictionary is returned containing key-value pairs. However, the structure
    for valid data is different from error notification.

    dOutput (dictionary)

        dOutput["sStatus"] = "ERROR"
            The string "ERROR" is returned under the "sStatus" key, to indicate
            that error information is available.

        dOutput["sErr_desc"] (string)
            Brief description of the error.

            "data validation": Incorrectly formatted input

            "item not found": Search yielded 0 results

            "connection error": Unable to reach the database

            "internal error": reserved for an error which could not be
                predicted at the design stage.

    Raises (exceptions)
    ------
    To be determined

    Example of correct use
    ------
    The dictionaries are written across multiple lines to highlight their
    structure.

    >>> dBriefcase = {
        "iIdx": 0,
        "iMax_res": 5,
        "sItem_filter": None
    }
    >>> dOutput = list_products(dBriefcase)
    >>> print(dOutput)
    {
        "sStatus":"OK",
        "iIdx_n":1,
        "iSearch_tot":2,
        "aItems":[
            {
                "sItem_id":"I-00001",
                "sBrand":"Vaenesston Zoo",
                "sDesc":"Female unicorn",
                "sSize":"Medium horse (16hh)",
                "sColour":"White",
                "fPrice":25000000.00,
                "sCurrency":"USD",
                "iStock":1,
                "dPhotos":[
                    "https://i.pinimg.com/564x/0c/6d/34/0c6d34398d9a464f6aafb6f8d32dee38.jpg"
                ]
            },
            {
                "sItem_id":"I-00002",
                "sBrand":"Handmade Flags",
                "sDesc":"Flag of Quidthovice",
                "sSize":"150cm x 100cm",
                "sColour":"State colours",
                "fPrice":14.99,
                "sCurrency":"PLN",
                "iStock":100,
                "dPhotos":[
                    "https://i.pinimg.com/originals/b4/5a/4c/b45a4c2bc6a626a269548e461ee84301.jpg"
                ]
            }
        ]
    }

    Example of error response
    ------
    The dictionaries are written across multiple lines to highlight their
    structure.

    >>> dBriefcase = {
        "iIdx": 0,
        "iMax_res": 5,
        "sItem_filter": Male unicorn
    }
    >>> dOutput = list_products(dBriefcase)
    >>> print(dOutput)
    {
        "sStatus":"ERROR",
        "sErr_desc":"item not found"
    }
    """

    pass
    # TODO: Add code here.
#-------------------------------------------------------------------------------
def create_order(sAuth_token):
    """Indicates the intention for the customer to make purchaces.

    Method validates the authentication token (to make sure that is hasn't
    expired). Internally, a 'basket' is opened under this authentication code.

    Architect's Note:\n
    I would place the customer authentication at this step. The customer would
    be free to browse the shop without any authentication. However, when it
    comes to a financial transaction, we need authentication. Since I don't
    understand the difference between 'create order' and 'update order', I made
    a few assumptions.
    Anyway, In my revised model, I would take in (in the briefcase): the user
    name, the salt of their password. Two level authentication can be done at
    the checkout stage (confirmation via SMS or another channel)

    Parameters
    ----------
        sAuth_token (string)
        Expiring cryptographic token generated during authentication.
            # Architect's Note:
            # Since the token expires within about 30 minutes, then I believe
            # that AES or triple-DES encryption should be sufficient. The token
            # can be encoded in base-62 (0..9,A..Z,a..z). Going RSA I think
            # would be overkill. However, the RSA option could be open as a
            # future security upgrade. If the traffic is lighter, then a simple
            # random number could be implemented.

    Returns - Valid data:
    --------
    A dictionary is returned containing key-value pairs. However, the structure
    for valid data is different from error notification. The 'sStatus' key is
    common to both 'valid data' and 'error' returns. It determines the further
    structure of the response

    dOutput (dictionary)

        dOutput["sStatus"] = "OK"
            A string "OK" is returned as the value to the key "OK". This is a
            flag to indicate that the request was successful.

        dOutput["sBasket_code"] (string)
            Cryptographic identifier to which "basket" to use.
            # Architect's Note:
            # Internally, the 'basket' will have the authentication code
            # attached to it. At check-out, the authentication will be checked
            # again.

    Returns - Error output:
    -------
    A dictionary is returned, which has one common key with the 'Valid data'
    return option.

    dOutput (dictionary)

        dOutput["sStatus"] = "ERROR"
            The string "ERROR" is populated to flag the condition.

        dOutput["sErr_desc"] (string)
            Brief description of error

            "unable to validate token": technical issue with validation process.

            "token expired": timestamp inside the token is now in the past.

            "invalid token": token returned does not match internal token.

    Raises (exceptions)
    ------
    To be determined

    Example of correct use
    ------
    >>> dOutput = create_order("8zQ74sSawCfWza05")
    >>> print(dOutput)
    {"sStatus":"OK", "sBasket_code":"sA13Qeqx"}

    Example of error response
    ------
    >>> dOutput = create_order("3zQ74sSawCfWza05")
    >>> print(dOutput)
    {"sStatus":"Error", "sErr_desc":"invalid token"}

    """
    pass
    # TODO: Add code here.
#-------------------------------------------------------------------------------
def update_order(dBriefcase):
    """ Requests the selected item to be reserved for purchasing.

    Parameters:
    ----------
        dBriefcase (dictionary)
        This is a container transporting other parameters. It contains the
        following keys:

            dBriefcase["sBasket_code"] (string)
                One-time cryptographic token used to identify the correct
                'basket'.

            dBriefcase["sItem_id"] (string)
                Identification code for the product being purchased.

            dBriefcase["iQty"] (integer)
                Number of items purchased.

    Returns - Valid data
    -------
    A dictionary is returned containing key-value pairs. However, the structure
    for valid data is different from error notification. The 'sStatus' key is
    common to both 'valid data' and 'error' returns. It determines the further
    structure of the response

    dOutput (dictionary)

        dOutput["sStatus"] = "OK"
            The string "OK" is returned under the "sStatus" key, to indicate
            that non-error data is available.

    Returns - Error output:
    -------
    A dictionary is returned, which has one common key with the 'Valid data'
    return option.

    dOutput (dictionary)

        dOutput["sStatus"] = "ERROR"
            The string "ERROR" is populated to flag the condition.

        dOutput["sErr_desc"] (string)
            Brief description of error

            "data validation": Syntax error in the input

            "item sold out": No stock is available at this time.

            "partial order": Customer ordered more than stock available.
                'Business rules' will deterimine how to handle this situation

            "not available": Business rules say that this item can't be sold to
                this customer. For example, a pneumatic pistol (pellet gun) may
                only be legally available in certain regions.

            "invalid currency": Business rules may say that a Polish customer
                is not allowed to purchase items quoted in, lets say "USD".

            "maximum quantity exceeded": Some items have limits on how much one
                customer may purchase. Going over that limit will trigger this
                response

            "item does not exist": dBriefcase['sItem_id'] does not exist.

            "invalid basket": token returned does not match internal token.

            "basket expired": Time limit has been exceeded in doing the shopping

    Raises (exceptions)
    ------
    To be determined

    Example of correct use
    ------
    The dictionaries are written across multiple lines to highlight their
    structure.

    >>> dBriefcase = {
        "sBasket_code": "sA13Qeqx",
        "sItem_id": "I-00002",         # Flag
        "iQty": 3
    }
    >>> dOutput = update_order(dBriefcase)
    >>> print(dOutput)
    {"sStatus":"OK"}

    Example of error response.
    ------
    >>> dBriefcase = {
        "sBasket_code": "sA13Qeqx",
        "sItem_id": "I-00001",         # Unicorn
        "iQty": 1
    }
    >>> dOutput = update_order(dBriefcase)
    >>> print(dOutput)
    {"sStatus":"ERROR", "sErr_desc":"invalid currency"}
    """
    pass
    # TODO: Add code here.
#-------------------------------------------------------------------------------
def delete_order(dBriefcase):
    """Requests a return of item from customer's basket prior to payment.

    Run 'list_orders' prior to this command. This will give the most up-to-date
    list of items.

    Parameters
    ---------
        dBriefcase (dictionary)
        This is an all-in-one container for transporting variables into the
        method. The keys required are listed below:

            dBriefcase["sBasket_code"] (string)
                Identifies from which basket we need to remove the items.

            dBriefcase["sItem_id"] (string)
                Identifier code for the item being removed

            dBriefcase["iQty"] (integer)
                Number of items to be removed. This allows to reduce the number
                of items in the basket, say from 3 to 2, by specifying '1'.
                Integers can't be negative or zero.

    Returns - Valid data:
    --------
    A dictionary is returned containing key-value pairs. However, the structure
    for valid data is different from error notification. The 'sStatus' key is
    common to both 'valid data' and 'error' returns. It determines the further
    structure of the response

    dOutput (dictionary)

        dOutput["sStatus"] = "OK"
            A string "OK" is returned as the value to the key "OK". This is a
            flag to indicate that the request was successful.

    Returns - Error output:
    -------
    A dictionary is returned, which has one common key with the 'Valid data'
    return option.

    dOutput (dictionary)

        dOutput["sStatus"] = "ERROR"
            The string "ERROR" is populated to flag the condition.

        dOutput["sErr_desc"] (string)
            Brief description of error

            "quantity too low": Attempt to remove 0 or a negative amount of
                items. Use "update order" to add additional units to an item.

            "quantity too high": Attempt to return too much. Triggered in this
                example, where the basket has 4 items, and we are trying to
                delete 5.

            "invalid basket": token returned does not match internal token.

            "basket expired": Time limit has been exceeded in doing the shopping

            "invalid item code": Trying to return a product which is not in the
                customer's basket.

    Raises (exceptions)
    ------
    To be determined

    Example of correct use
    ------
    The dictionaries are written across multiple lines to highlight their
    structure.

    >>> dBriefcase = {
        "sBasket_code": "sA13Qeqx",
        "sItem_id": "I-00002",         # Flag
        "iQty": 1                      # 3 -> 2 in the basket
    }
    >>> dOutput = update_order(dBriefcase)
    >>> print(dOutput)
    {"sStatus":"OK"}

    Example of error response
    ------
    The dictionaries are written across multiple lines to highlight their
    structure.

    >>> dBriefcase = {
        "sBasket_code": "sA13Qeqx",
        "sItem_id": "I-00001",         # Unicorn
        "iQty": 1
    }
    >>> dOutput = update_order(dBriefcase)
    >>> print(dOutput)
    {"sStatus":"ERROR", "sErr_desc":"invalid item code"}
    """

    pass
    # TODO: Add code here.

#-------------------------------------------------------------------------------
def checkout_order(dBriefcase):
    """Finalizes the shopping experience.

    The basket is 'sealed' and no more changes are allowed after this command.
    Destroys the 'sBasket_code', but creates a human-readable invoice code.

    Parameters:
    ----------
        dBriefcase (dictionary)
        This is a container transporting other parameters. It contains the
        following keys:

            dBriefcase["sBasket_code"] (string)
                One-time cryptographic token used to identify the correct
                'basket'.

            dBriefcase["sAuth_token"] (string)
                Re-identification of the customer. It is done to have redundancy
                in the security system.

    Returns - Valid data:
    --------
    A dictionary is returned containing key-value pairs. However, the structure
    for valid data is different from error notification. The 'sStatus' key is
    common to both 'valid data' and 'error' returns. It determines the further
    structure of the response

    dOutput (dictionary)

        dOutput["sStatus"] = "OK"
            A string "OK" is returned as the value to the key "OK". This is a
            flag to indicate that the request was successful.

        dOutput["sInv_Currency"] (string)
            ISO-4217 code ("PLN", "USD", "XBT", ect) of the invoice. This is
            the currency of the invoice. All financial amounts use these units.

        dOutput["fShip_cost"] (float)
            Amount charged for delivery of goods.

        dOutput["fGoods_cost"] (float)
            Total money charged for items purchased on the site.

        dOutput["sInvoice_code"] (string)
            Invoice reference number. This will be needed by the customer to
            validate collection.

    Returns - Error output:
    -------
    A dictionary is returned, which has one common key with the 'Valid data'
    return option.

    dOutput (dictionary)

        dOutput["sStatus"] = "ERROR"
            The string "ERROR" is populated to flag the condition.

        dOutput["sErr_desc"] (string)
            Brief description of error

            "unable to validate auth token": technical issue with validation.
                Transaction still open. Additional expiry time will be given.

            "auth token expired": The authentication token has expired, even
                taking the amount of time to do shopping into account. This
                indicates that the 'sBasket_code' token has also expired. Hence
                the transaction is completely rejected.

            "invalid auth token": token returned does not match internal token.
                Transaction is completely rejected.

            "unable to validate basket token": technical issue with validation.
                Transaction still open. Additional expiry time will be given.

            "basket token expired": The basket token has expired. Customers
                have a certain amount of time to complete their shopping. This
                time is determined by Business rules. Hence the transaction is
                completely rejected.

            "invalid basket token": token returned does not match internal data.
                Transaction is completely rejected.

            "unable to generate invoice": Technical problems with the financial
                side of the site. Additional expiry time will be given.

            "payment rejected": Customer was unable to settle the invoice. The
                transaction is completely rejected.

    Example of correct use
    ------
    The dictionaries are written across multiple lines to highlight their
    structure.

    >>> dBriefcase = {
        "sBasket_code": "sA13Qeqx",
        "sAuth_token": "8zQ74sSawCfWza05",
        }
    >>> dOutput = checkout_order(dBriefcase)
    >>> print(dOutput)
    {
        "sStatus":"OK",
        "sInv_Currency":"PLN",
        "fShip_cost":40.00,
        "fGoods_cost":29.98,
        "sInvoice_code":"Z-000012"
    }

    Example of error response.
    ------
    The dictionaries are written across multiple lines to highlight their
    structure.

    >>> dBriefcase = {
        "sBasket_code": "5A13Qeqx",
        "sAuth_token": "8zQ74sSawCfWza05",
        }
    >>> dOutput = checkout_order(dBriefcase)
    >>> print(dOutput)
    {"sStatus":"ERROR", "sErr_desc":"invalid basket token"}

    """
    pass

#-------------------------------------------------------------------------------
def list_orders(sBasket_code):
    """Gives customer access to the items in their 'basket'.

    Returns a structure which includes all the items which the customer intends
    to purchase. This is the net result of 'update_order' and 'delete_order'

    Parameters
    -------
    sBasket_code (string)

        Single-use cryptographic code which joins items purchased with the
        purchaser

            # Architect's Note: I try not to repeat definitions which were used
            # in a previous field. From experience, it is always helpful to have
            # multiple definitions of a certain item. Also, not every person's
            # English is good. Alternative descriptions will assist in a better
            # understanding of the concept.

    Returns - Valid data:
    -------
    A dictionary is returned containing key-value pairs. However, the structure
    for valid data is different from error notification. The 'sStatus' key is
    common to both 'valid data' and 'error' returns. It determines the further
    structure of the response\n
    Architect's Note: I have omitted the sub-total and the delivery fee. The
    decision is left to "business rules" if this data should be included at this
    stage. Also, the frontend would be able to do this calculation.

    dOutput (dictionary)

        dOutput["sStatus"] = "OK"
            The string "OK" is returned under the "sStatus" key, to indicate
            that non-error data is available.

        dOutput["aItems"] (list of dictionaries)
            Lists items reserved for purchace. Each item in the list has the
            following structure. The 'n' (integer) in the structure indexes the
            item number on the list

            dOutput["aItems"][n]["sItem_id"] (string)
                Identifier of the item purchased.

            dOutput["aItems"][n]["iQty"] (integer)
                How many items are on order

            dOutput["aItems"][n]["sDesc"] (string)
                Description of the item

            dOutput["aItems"][n]["sSize"] (string)
                If the item (like clothing or shoes) comes in various sizes, it
                is specified here.

            dOutput["aItems"][n]["sColour"] (string)
                Main colour or pattern of the item.

            dOutput["aItems"][n]["sItem_currency"] (string)
                ISO-4217 currency code for the items purchased. Usually it is
                the currency of the customer's region.

            dOutput["aItems"][n]["fUnit_price"] (float)
                Price of the single item in the "sCurrency"

            dOutput["aItems"][n]["fTotal_price"] (float)
                Price for all the copies of the item.

    Returns - Error output:
    -------
    A dictionary is returned, which has one common key with the 'Valid data'
    return option.

    dOutput (dictionary)

        dOutput["sStatus"] = "ERROR"
            The string "ERROR" is populated to flag the condition.

        dOutput["sErr_desc"] (string)
            Brief description of error

            "unable to validate token": technical issue with validation process.

            "token expired": timestamp inside the token is now in the past.

            "invalid token": token returned does not match internal token.

    Raises (exceptions)
    ------
    To be determined

    Example of correct use
    ------
    The dictionaries are written across multiple lines to highlight their
    structure.

    >>> dOutput = list_orders("sA13Qeqx")
    >>> print(dOutput)
    {
        "sStatus":"OK",
        "aItems":[
            {
                "sItem_id":"I-00002",
                "iQty":3,
                "sDesc":"Flag of Quidthovice",
                "sSize":150cm x 100cm",
                "sColour":"State colours",
                "sItem_currency":"PLN",
                "fUnit_price":"14.99",
                "fTotal_price":"44.97"
            },
            {
                ...
            }
        ]
    }

    Example of error response
    -------
    >>> dOutput = list_orders("5A13Qeqx")
    >>> print(dOutput)
    {"sStatus":"Error", "sErr_desc":"invalid token"}

    """
    pass
    # TODO: Add code here.
#-------------------------------------------------------------------------------
print("This is a dummy program concentrating on the input / output of each " +
"function.")
