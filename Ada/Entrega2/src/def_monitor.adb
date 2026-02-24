with Text_Io;
use  Text_Io;

package body def_monitor is

   protected body MonitorCoches is
      
      --Permite que los coches que esperan en el norte,entren.
      entry AccesoNorte(indice:in Integer) when (num_cochesN_espera >=num_cochesS_espera 
                                         and puente_ocupado=False and ambulancia_espera=False) is                                  
      begin
      num_cochesN_espera := num_cochesN_espera- 1;
      Put_line("El cotxe " & indice'Img & " entra al pont. Esperen al NORD: " & num_cochesN_espera'Img);
      puente_ocupado := True;
         
      end AccesoNorte;
     
        
      --Se utiliza cuando un vehículo está esperando para entrar desde el norte.
      procedure EsperaNorte(indice:in Integer) is
      begin
         num_cochesN_espera:=num_cochesN_espera + 1;
         Put_line("El cotxe " & indice'Img &" espera a l'entrada NORD , esperen al NORD: " & num_cochesN_espera'Img &" ");  
      end;
        
        
              
        
      --Permite que los coches que esperan en el sur,entren.
      entry AccesoSur(indice:in Integer) when (num_cochesS_espera >num_cochesN_espera 
                                         and puente_ocupado=False and ambulancia_espera=False) is                                  
      begin
         num_cochesS_espera := num_cochesS_espera - 1;
         Put_line("El cotxe " & indice'Img & " entra al pont. Esperen al SUD: " & num_cochesS_espera'Img);
      puente_ocupado := True;
        
      end AccesoSur;
            
      --Indica cuando un vehículo está esperando a entrar desde el sur.
      procedure EsperaSur(indice:in Integer) is
      begin
         num_cochesS_espera:=num_cochesS_espera + 1;
         Put_line("El cotxe " & indice'Img & " espera a l'entrada SUD , esperen al SUD: " & num_cochesS_espera'Img);
      end EsperaSur;
         
      --Permite que los coches que esperan en el sur,entren.
      entry AccesoAmbulancia(Indice:in Integer) when (puente_ocupado=False) is                                  
      begin
      
      Put_line("+++++Ambulància "& Indice'Img & " és al pont");
      ambulancia_espera:=False;
      puente_ocupado := True;
      end AccesoAmbulancia;  
      
        --Indica cuando la ambulancia está esperando a entrar, sea en el norte o en el sur.
      procedure EsperaAmbulancia(Indice : in Integer) is
      begin
         ambulancia_espera := True;
         Put_line("+++++L'ambulancia " & Indice'img & " espera per entrar");
      end EsperaAmbulancia;
      
      
      
      --Se utiliza para permitir el siguiente acceso.
      procedure DesbloqueoPuente(Indice: in Integer) is 
      begin
         Put_line("----->El vehicle " & Indice'img & " surt del pont");
         puente_ocupado:=False; 
      end DesbloqueoPuente;

      
   
   end MonitorCoches;
      
   

end def_monitor;
