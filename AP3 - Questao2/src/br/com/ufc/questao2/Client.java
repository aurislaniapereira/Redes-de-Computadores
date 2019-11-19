package br.com.ufc.questao2;

import java.rmi.Naming;

public class Client {
	public static void main(String[] args) {
		try {
			Servico s = (Servico) Naming.lookup("//127.0.0.1:1020/Servico");
			System.out.println("Hora e data: " + s.getDataHora());
		} catch (Exception e) {
			System.out.println(e);
		}
	}
}
