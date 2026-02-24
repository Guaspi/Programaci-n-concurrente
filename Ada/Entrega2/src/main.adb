with Text_Io;
use  Text_Io;
with def_monitor;
use def_monitor;
with Ada.Numerics.Float_Random;
use Ada.Numerics.Float_Random;


procedure Main is

   num_coches : constant Integer := 5;
   type dir is (NORD,SUD);

   monitor: MonitorCoches; --PROTEGIDO--


  -----------UTILIZADO PARA CREAR SLEEPS "ALEATORIOS" (ENTRE UN MARGEN) -----------
   --------------------------------------------------
    procedure sleep_aleatorio(max: Float) is
      Generador:Generator;

      function Numero_Aleatorio return Float is ---- Genera un número aleatorio entre 1 y 5
         FloatRAND : constant Float := Random(Generador);
      begin
         return (FloatRAND * max) + 1.0;
      end Numero_Aleatorio;
   ---------------------------------------------------
   begin
      Reset(Generador);
      -- Espera el número aleatorio de segundos
      delay Duration(Numero_Aleatorio);
   end sleep_aleatorio;



   task type vehiculos is
      entry Start(Indice: in Integer; direccion: in dir);
   end vehiculos;

   task body vehiculos is
      this_Indice: Integer;
      this_direccion: dir;


   begin
      accept Start (Indice : in Integer; direccion : in dir) do
         this_Indice:= Indice;
         this_direccion:=direccion;
      end Start;

      sleep_aleatorio(5.0); --El temps que cada vehicle espera a posar-se en marxa
      if this_Indice= 112 then
         Put_Line("L'ambulancia " & this_Indice'Img & " està en ruta");

         sleep_aleatorio(5.0);

         monitor.EsperaAmbulancia(this_Indice);
         monitor.AccesoAmbulancia(this_Indice);
           sleep_aleatorio(5.0);
         monitor.DesbloqueoPuente(this_Indice);

      elsif this_Indice mod 2 = 0 then
           this_direccion:= NORD;
           Put_Line("El cotxe "& this_Indice'Img & " està en ruta en direcció " & this_direccion'Img);
         sleep_aleatorio(5.0);
         monitor.EsperaNorte(this_Indice);
         monitor.AccesoNorte(this_Indice);
           sleep_aleatorio(5.0);
         monitor.DesbloqueoPuente(this_Indice);

      else
         this_direccion:=SUD;
         Put_Line("El cotxe "& this_Indice'Img &" està en ruta en direcció "& this_direccion'Img);
           sleep_aleatorio(5.0);
           monitor.EsperaSur(this_Indice);
         monitor.AccesoSur(this_Indice);
           sleep_aleatorio(5.0);
         monitor.DesbloqueoPuente(this_Indice);

      end if;
   end vehiculos;


   --------HILOS--------

   THREADS : constant Integer := num_coches + 1; --el 1 se refiere a la ambulancia

   type hilos_coches is array (1..THREADS) of vehiculos;
   hilos: hilos_coches;

   type array_indices is array (Positive range <>) of Integer;

   IDs:array_indices := (1, 2, 3, 4, 5, 112);  ---son los indices que se pasan por paramétro.


begin

   for i in 1..THREADS loop
      hilos(i).Start(IDs(i),NORD);
   end loop;

end Main;
