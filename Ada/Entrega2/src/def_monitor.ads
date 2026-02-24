package def_monitor is
   
   
   
----Declaración de los entrys y de los procedures utilizados en def_monitor.adb
   protected type MonitorCoches is
      
      entry AccesoNorte(indice : in Integer) ;
      entry AccesoSur(indice : in Integer) ;
      entry AccesoAmbulancia(indice : in Integer);
      procedure EsperaNorte(indice : in Integer) ;
      procedure EsperaSur(indice : in Integer) ;
      procedure EsperaAmbulancia(indice : in Integer);
      procedure DesbloqueoPuente(indice : in Integer);
      ---declaració de les variables privades protegides
    private
   
      num_cochesN_espera: Integer :=0;
      num_cochesS_espera: Integer :=0;
      ambulancia_espera : Boolean := False;
      puente_ocupado: Boolean :=False;
 
   end MonitorCoches;


end def_monitor;
