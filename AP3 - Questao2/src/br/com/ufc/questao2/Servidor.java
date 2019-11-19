package br.com.ufc.questao2;

import java.rmi.Naming;

public class Servidor {

	Servidor(){
		try {
			Servico s = new Servente();
			Naming.rebind("RMI://127.0.0.1:1020/Servico", s);
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		new Servidor();
	}

}
