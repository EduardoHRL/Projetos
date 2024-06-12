package DAO;

import Factory.ConnectionFactory;
import Modelo.Usuario;
import java.sql.*;
import java.sql.PreparedStatement;
import Gui.FormUsuario;
import java.util.List;
import java.util.ArrayList;
import javax.swing.table.DefaultTableModel;

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

    public List<Usuario> consultarTodos() {
        String sql = "SELECT * FROM tbl_usuario";
        List<Usuario> usuarios = new ArrayList<>();

        try {

            PreparedStatement stmt = connection.prepareStatement(sql);
            ResultSet resultado = stmt.executeQuery();
            while (resultado.next()) {
                Usuario usuario = new Usuario();
                usuario.setId(resultado.getLong("id"));
                usuario.setNome(resultado.getString("nome"));
                usuario.setCpf(resultado.getString("cpf"));
                usuario.setEmail(resultado.getString("email"));
                usuario.setTelefone(resultado.getString("telefone"));
                usuarios.add(usuario);
            }
            resultado.close();
            stmt.close();
        } catch (SQLException ex) {
            throw new RuntimeException(ex);
        }
        return usuarios;
    }
    public static List<usuario> getUsuario() {
        return usuarios
    }
            
    
    
    
    
}
