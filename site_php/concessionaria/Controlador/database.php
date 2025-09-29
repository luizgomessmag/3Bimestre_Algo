<?php
require_once "config.php";
require_once '../Modelo/pessoa.php';

class Database
{
    private $conn;

    public function __construct() {
        try{
            //conexão ao mysql sem definir o banco
            $this->conn = new PDO("mysql:host=".DB_HOST,
                 DB_USER, DB_PASS);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE,
                PDO::ERRMODE_EXCEPTION);

            //criação do banco se não existir
            $this->conn->exec("CREATE DATABASE IF NOT EXISTS ".DB_NAME);

            //Conectar ao banco
            $this->conn = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME,
                DB_USER, DB_PASS);
        } catch (PDOException $e) {
            die("Erro de conexão: " . $e->getMessage());
        }
    }

    public function criarTabela($comando) {
        /**
         *   " usuarios(
         *   id INT AUTO_INCREMENT PRIMARY KEY,
         *   nome VARCHAR(100) NOT NULL,
         *   email VARCHAR(100) UNIQUE NOT NULL)
         * "
         */
        try {
            $sql = "CREATE TABLE IF NOT EXISTS $comando";
            $this->conn->exec($sql);
            echo "Tabela criada/verificada com sucesso.<br>";
        } catch (PDOException $e) {
            echo "Erro ao criar tabela: " . $e->getMessage();
        }
    }

    // Inserir registros (genérico)
    public function inserir($tabela, $dados) {
        
        // $tabela = "usuarios"
        // $dados = ["nome" => "João", "email" => "joao@gmail.com"]
        
        $colunas = implode(", ", array_keys($dados));
        $placeholders = ":" . implode(", :", array_keys($dados));

        
    }

    public function buscarTodos($tabela){
            $sql = "select * from $tabela";
            $stmt = $this->conn->query($sql);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        }

        
        public function buscar($sql) {
        $stmt = $this->conn->query($sql);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

        public function atualizar($tabela, $dados, $condicao){

            $sql =  "UPDATE $tabela SET ($colunas) VALUES ($placeholders) WHERE $condicao";
            
            $stmt = $this->conn->prepare($sql);
            $stmt->execute($dados);

        }

        public function deletar($tabela, $id){

            $sql = "DELETE FROM $tabela WHERE id = :id";

            $stmt = $this->conn->preparate($sql);
            $stmt->execute([":id" => $id]);
        }

}