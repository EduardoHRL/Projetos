package DAO;

import Factory.ConnectionFactory;
import Modelo.Usuario;
import java.sql.*;
import java.sql.PreparedStatement;
import Gui.FormUsuario;

public class UsuarioDao {

    private Connection connection;

    Long id;
    String nome;
    String cpf;
    String email;
    String telefone;

    public UsuarioDao() {
        this.connection = new ConnectionFactory().getConnection();
    }

    public void adiciona(Usuario usuario) {
        String sql = "INSERT INTO tbl_usuario(nome,cpf,email,telefone) VALUES(?,?,?,?)";

        try {
            PreparedStatement stmt = connection.prepareStatement(sql);
            stmt.setString(1, usuario.getNome());
            stmt.setString(2, usuario.getCpf());
            stmt.setString(3, usuario.getEmail());
            stmt.setString(4, usuario.getTelefone());
            stmt.execute();
            stmt.close();
        } catch (SQLException u) {
            throw new RuntimeException(u);
        }
    }

    public void consulta(Usuario usuario) throws SQLException {
        String query = "SELECY * FROM tbl_usuario";

        try {
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(query);

            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String nome = resultSet.getString("nome");
                int cpf = resultSet.getInt("cpf");
                String email = resultSet.getString("email");
                String telefone = resultSet.getString("telefone");

                FormUsuario tabela = new FormUsuario();

                Object[] rowData = {nome, cpf, email, telefone};
                tabela.Tabela(rowData);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Fechar a conexão com o banco de dados
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        }
    }
}
