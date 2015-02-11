Market Snitch
============
A market research tool for PhilGEPs(http://philgeps.gov.ph/) designed to help facilitate the creation of accurate budget estimates based on current market prices.

It's main goal is to help erradicate or minimize overbudgeting for government procurement projects.

Features:
1. Market Price Comparison
Price Comparison against current market data
2. Historical Price Comparison
Price Comparison against historical price data gathered from previous awards
3. APIs
APIs for Organization, Awards, Bidders List, Bid Line Item and Bid Information


## Prerequisites


### External libs for Pillow

See: https://pillow.readthedocs.org/en/latest/installation.html#simple-installation

```
$ sudo apt-get install libtiff4-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk
```


### Virtualenv

You should have a virtualenv ready with either Python 2.7.x or 3.x


### Database

This app is configured with PostgreSQL/MySQL in mind.


### Configuration

Under your project's settings folder you'll find a `config.json` file. Fill it out with the needed
values. Alternatively you can also create a `config-user.json` for configurations specific to a
particular environment.


### Server settings

TODO

