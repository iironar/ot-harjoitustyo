import unittest

from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        
        
            
    def test_kortin_lataus_toimii_oikein(self):
        virhe = "kortin lataus ei toimi oikein"
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+500, virhe)
        self.assertEqual(self.maksukortti.saldo, 1500, virhe)
        
    def test_kortin_lataus_toimii_oikein_negatiivisella_maaralla(self):
        virhe = "kortin lataus ei toimi oikein"
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1),None,virhe)
         
    
    def test_kassan_korttiosto_toimii_edullisella_kun_maksu_riittava(self):
        virhe = "Korttiosto ei toimi edullisella kun maksu riittava"
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000, virhe)
        self.assertEqual(self.kassapaate.edulliset, 1, virhe)
        self.assertEqual(self.maksukortti.saldo, 1000-240, virhe)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True, virhe)
    
    def test_kassan_korttiosto_toimii_edullisella_kun_maksu_ei_riittava(self):
        virhe = "Korttiosto ei toimi edullisella kun maksu ei riittava"
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000, virhe)
        self.assertEqual(self.kassapaate.edulliset, 0, virhe)
        self.assertEqual(self.maksukortti.saldo, 200, virhe)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False, virhe)    
        
        
    def test_kassan_korttiosto_toimii_maukkaalla_kun_maksu_riittava(self):
        virhe = "Korttiosto ei toimi maukkaalla kun maksu ei riittava"
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000, virhe)
        self.assertEqual(self.kassapaate.maukkaat, 1, virhe)
        self.assertEqual(self.maksukortti.saldo, 1000-400, virhe)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True, virhe)
    
    def test_kassan_korttiosto_toimii_maukkaalla_kun_maksu_ei_riittava(self):
        virhe = "Korttiosto ei toimi maukkaalla kun maksu riittava"
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000, virhe)
        self.assertEqual(self.kassapaate.maukkaat, 0, virhe)
        self.assertEqual(self.maksukortti.saldo, 200, virhe)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False, virhe)    
    
        
                                
                             
    def test_kassan_saldo_oikein_luontihetkellä(self):
        virhe = "saldo ei täsmää luontihetkellä"
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000, virhe)
        self.assertEqual(self.kassapaate.edulliset, 0, virhe)
        self.assertEqual(self.kassapaate.maukkaat, 0, virhe)
        
    def test_kassan_kateisosto_toimii_edullisella_maksu_riittava(self):    
        virhe = "käteisosto ei toimi edullisella kun maksu riittää"
        maksu = 240
        maksu = self.kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240, virhe)
        self.assertEqual(self.kassapaate.edulliset, 1, virhe)
        self.assertEqual(maksu, 0, virhe)
        
        
    def test_kassan_kateisosto_toimii_edullisella_maksu_ei_riita(self):    
        virhe = "käteisosto ei toimi edullisella kun maksu ei riitä"
        maksu = 120
        self.kassapaate.syo_edullisesti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000, virhe)
        self.assertEqual(self.kassapaate.edulliset, 0, virhe)
        self.assertEqual(maksu, 120, virhe)
        
    def test_kassan_kateisosto_toimii_maukkaalla_maksu_riittava(self):    
        virhe = "käteisosto maukkaalla ei toimi kun maksu riittävä"
        maksu = 400
        maksu = self.kassapaate.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400, virhe)
        self.assertEqual(self.kassapaate.maukkaat, 1, virhe)
        self.assertEqual(maksu, 0, virhe)
        
    def test_kassan_kateisosto_toimii_maukkaalla_maksu_ei_riita(self):    
        virhe = "käteisosto maukkaalla ei toimi kun maksu ei riitä"
        maksu = 120
        self.kassapaate.syo_maukkaasti_kateisella(maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000, virhe)
        self.assertEqual(self.kassapaate.maukkaat, 0, virhe)
        self.assertEqual(maksu, 120, virhe)                     
        
        
   
        
            