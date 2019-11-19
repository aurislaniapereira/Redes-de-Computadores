package br.com.ufc.questao2;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.text.SimpleDateFormat;
import java.util.Calendar;

public class Servente extends UnicastRemoteObject implements Servico{
	
	protected Servente() throws RemoteException {
		super();
	}

	public String getDataHora() throws RemoteException {
		SimpleDateFormat stf= new SimpleDateFormat("dd/MM/yyyy HH:mm");
		return stf.format(Calendar.getInstance().getTime());
	}


}
