import unittest
from xmlunittest import XmlTestCase
from lxml import etree

class XmlParses(XmlTestCase):

    def setUp(self):
        self.xml_filepath = "home/jedmondson/PycharmProjects/XmlToPdfBuilder/source/xml/example.xml"
        self.parsedxml = etree.parse(self.xml_filepath)
        self.docroot = self.parsedxml.getroot()
        self.graphicsrc_iter = self.docroot.getiterator(tag='graphic.source')
        self.varsrc_iter = self.docroot.getiterator(tag='variable.source')
        data = etree.tostring(self.parsedxml)
        self.root = self.assertXmlDocument(data)
        self.error_info = []
        # except IOError:
        # print "The specified file does not exist or is unreadable"
        # except etree.XMLSyntaxError:
        # print "The specified xml file is not well formed"

    def test_docTitleExists(self):
        try:
            self.assertXpathsExist(self.root,('. /variable.list.group/variable.list/variable.source/@variable.name="doc.title"',), "custom error message")
            # self.longMessage
        except:
            self.error_info.append('Doc title missing')

    def test_copyrightStmntExists(self):
        try:
            self.assertXpathsExist(self.root,('. /variable.list.group/variable.list/variable.source/@variable.name="copyright.statement"',))
        except:
            self.error_info.append('Copyright statement missing')

    def test_hpIconExists(self):
        try:
            self.assertXpathsExist(self.root,('./variable.list.group/graphic.list/graphic.source/@graphic.name="hp.icon"',))
        except:
            self.error_info.append('HP icon missing')

    def test_productImgExists(self):
        try:
            self.assertXpathsExist(self.root,('./variable.list.group/graphic.list/graphic.source/@graphic.name="product.image"',))
        except:
            self.error_info.append('Product image missing')

    def test_printedInStmntExists(self):
        try:
            self.assertXpathsExist(self.root,('./variable.list.group/graphic.list/graphic.source/@graphic.name="printed.in.statement"',))
        except:
            self.error_info.append('Printed in statment missing')

    def test_printedOnStmntExists(self):
        try:
            self.assertXpathsExist(self.root,('./variable.list.group/graphic.list/graphic.source/@graphic.name="printed.on.statement"',))
        except:
            self.error_info.append('Printed on statement missing')

    def test_barcodeExists(self):
        try:
            self.assertXpathsExist(self.root,('./variable.list.group/graphic.list/graphic.source/@graphic.name="barcode"',))
        except:
            self.error_info.append('DoBarcode graphice missing')

    # def test_xmlObjCreated(self):
    #     try:
    #         self.assertXpathsExist(self.root,('./variable.list.group/graphic.list/graphic.source/@graphic.name="hp.icon"',
    #                                      '. /variable.list.group/graphic.list/graphic.source/@graphic.name="info.icon"',
    #                                      '. /variable.list.group/graphic.list/graphic.source/@graphic.name="product.image"',
    #                                      '. /variable.list.group/graphic.list/graphic.source/@graphic.name="printed.in.statement"',
    #                                      '. /variable.list.group/graphic.list/graphic.source/@graphic.name="printed.on.statement"',
    #                                      '. /variable.list.group/graphic.list/graphic.source/@graphic.name="barcode"',
    #                                      '. /variable.list.group/variable.list/variable.source/@variable.name="doc.title"',
    #                                      '. /variable.list.group/variable.list/variable.source/@variable.name="copyright.statement"',
    #                                      'body/chapter.context/chapter/section.body/task'))
    #
    #         for graphic in self.graphicsrc_iter:
    #             elem = graphic.xpath('graphic/graphic.unit.group/graphic.unit.print.pdf/graphic.object')[0]
    #             self.assertXmlHasAttribute(elem, 'file.loc', expected_values=('../graphics/print/hp.eps',
    #                                                                           '../graphics/print/info.eps',
    #                                                                           '../graphics/print/product_info.eps',
    #                                                                           '../graphics/print/printedinchina.eps',
    #                                                                           '../graphics/print/printedon.eps',
    #                                                                           '../graphics/print/barcode.eps'))
    def tearDown(self):
        del(self.parsedxml)
        del(self.docroot)

if __name__ == '__main__':
    unittest.main()



