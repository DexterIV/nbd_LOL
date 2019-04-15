package main.java;

import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.ResultSet;
import com.datastax.driver.core.Session;
import main.java.dataUtils.FileLoader;

import java.util.List;

public class App {
    public static void main(String[] args) {


        // run docker cassandra with "docker run -p 9042:9042 --rm --name aCassandra -e cassandra:3.11"
        // when aCassandra is some name
        // if docker is already connected run "docker start aCassandra"
        // to get into docker bash run "docker exec -it aCassandra bash" and to execute queries use cqlsh
        String serverIP = "0.0.0.0";

        Cluster cluster = Cluster.builder()
                .addContactPoints(serverIP)
                .withPort(9042)
                .build();

        Session session = cluster.connect();


        System.out.println("connected");

        var jsons = FileLoader.getJSONResources();
        System.out.println(FileLoader.getJSONResources().size());

        session.execute("CREATE KEYSPACE IF NOT EXISTS \"league\""
                + "WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 3};");
        System.out.println("keyspace created");
        String query = "CREATE TABLE IF NOT EXISTS league.plays(\n" +
                "   gameid               text   PRIMARY KEY \n" +
                "   ,datablob               text\n"+
                ");";


        System.out.println("created table " + session.execute(query).toString());

        for (var jsonEntry: jsons.entrySet()) {
            session.execute("INSERT INTO league.plays (gameid, datablob) \n"
                    +"VALUES ('" + jsonEntry.getKey() + "', '" + jsonEntry.getValue() + "');");
        }
        System.out.println("Inserted data");

    }
}