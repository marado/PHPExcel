# About this fork

This PHPExcel fork only exists so you can have an easy way to get pear packages
of it, until upstream moves towards a new working pear channel.

You can install the package by downloading the file in Build/release/ (eg:
PHPExcel-1.0.8.20140428.tgz ), and then simply running:

 pear install PHPExcel-1.0.8.20140428.tgz

## Dependences

You can find one of the dependencies on this Pear Channel:
http://pear.cakephp.org/

# About PHPExcel

If you want to know more about PHPExcel:
http://phpexcel.codeplex.com/

If you want to see the official PHPExcel repository:
https://github.com/PHPOffice/PHPExcel

## The Original README

### PHPExcel - OpenXML - Read, Write and Create spreadsheet documents in PHP - Spreadsheet engine
PHPExcel is a library written in pure PHP and providing a set of classes that allow you to write to and read from different spreadsheet file formats, like Excel (BIFF) .xls, Excel 2007 (OfficeOpenXML) .xlsx, CSV, Libre/OpenOffice Calc .ods, Gnumeric, PDF, HTML, ... This project is built around Microsoft's OpenXML standard and PHP.

Master: [![Build Status](https://travis-ci.org/PHPOffice/PHPExcel.png?branch=master)](http://travis-ci.org/PHPOffice/PHPExcel)

Develop: [![Build Status](https://travis-ci.org/PHPOffice/PHPExcel.png?branch=develop)](http://travis-ci.org/PHPOffice/PHPExcel)

#### File Formats supported

##### Reading
 * BIFF 5-8 (.xls) Excel 95 and above
 * Office Open XML (.xlsx) Excel 2007 and above
 * SpreadsheetML (.xml) Excel 2003
 * Open Document Format/OASIS (.ods)
 * Gnumeric
 * HTML
 * SYLK
 * CSV

##### Writing
 * BIFF 8 (.xls) Excel 95 and above
 * Office Open XML (.xlsx) Excel 2007 and above
 * HTML
 * CSV
 * PDF (using either the tcPDF, DomPDF or mPDF libraries, which need to be installed separately)


#### Requirements
 * PHP version 5.2.0 or higher
 * PHP extension php_zip enabled (required if you need PHPExcel to handle .xlsx .ods or .gnumeric files)
 * PHP extension php_xml enabled
 * PHP extension php_gd2 enabled (optional, but required for exact column width autocalculation)


#### Want to contribute?
Fork us!

#### License
PHPExcel is licensed under [LGPL (GNU LESSER GENERAL PUBLIC LICENSE)](https://github.com/PHPOffice/PHPExcel/blob/master/license.md)
