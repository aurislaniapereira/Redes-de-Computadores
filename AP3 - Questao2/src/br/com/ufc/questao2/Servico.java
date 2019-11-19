package br.com.ufc.questao2;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Servico extends Remote{
	
	public String getDataHora() throws RemoteException;
	
}
