using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lab1
{
    public partial class Form1 : Form
    {
        private SqlConnection dbConnection;
        private SqlDataAdapter daPlayer, daCard;
        private DataSet tableData;
        private DataRelation drPlayerCard;

        BindingSource bsPlayer, bsCard;

        public Form1()
        {
            InitializeComponent();
        }

        private void ReloadDrinkTypesTableView()
        {
            if (tableData.Tables["Card"]!=null)
                tableData.Tables["Card"].Clear();

            daCard.Fill(tableData, "Card");
            dgvCards.DataSource = bsCard;
            
        }

        private void ConnectButton_Click_1(object sender, EventArgs e)
        {
            dbConnection = new SqlConnection("Data Source=PAULIE\\SQLEXPRESS;Initial Catalog=DBMS_Exam;Integrated Security=True");
            dbConnection.Open();

            daPlayer = new SqlDataAdapter("SELECT * FROM Player", dbConnection);
            tableData = new DataSet();
            daPlayer.Fill(tableData, "Player");
            dgvPlayers.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            daCard = new SqlDataAdapter("SELECT * FROM Card", dbConnection);
            daCard.Fill(tableData, "Card");
            dgvCards.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            DataColumn managerIdPlayer= tableData.Tables["Player"].Columns["pid"];
            DataColumn managerIdCard= tableData.Tables["Card"].Columns["cid"];
            drPlayerCard = new DataRelation("FK_Player_Card", managerIdPlayer, managerIdCard, false);
            tableData.Relations.Add(drPlayerCard);

            bsPlayer = new BindingSource();
            bsPlayer.DataSource = tableData;
            bsPlayer.DataMember = "Player";

            bsCard = new BindingSource();
            bsCard.DataSource = bsPlayer;
            bsCard.DataMember = "FK_Player_Card";
            dgvPlayers.DataSource = bsPlayer;

        }

        private void DistributorsView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void AddButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("INSERT INTO DrinkTypes (Type, DIStrid)"+
                "VALUES (@TYPE, @DIStrID)",dbConnection);

            
            try
            {
                //int DTypeid = Int32.Parse(DTypeIdBox.Text);
                if (tracerBox.Text.Length != 0)
                {
                    int DStrid = Int32.Parse(tracerBox.Text);

                    command.Parameters.Add("@TYPE", SqlDbType.VarChar);
                    command.Parameters["@TYPE"].Value = pIdBox.Text;

                    command.Parameters.Add("@DIstrID", SqlDbType.Int);
                    command.Parameters["@DIStrID"].Value = DStrid;

                    try
                    {
                        daCard.InsertCommand = command;
                        daCard.InsertCommand.ExecuteNonQuery();
                        ReloadDrinkTypesTableView();
                    }
                    catch (SqlException sqlException)
                    {
                        if (sqlException.Number == 2627)
                            MessageBox.Show("The drinkType id must be unique!");
                        else if (sqlException.Number == 547)
                            MessageBox.Show("There's no distributor with the given id!");
                        else
                            MessageBox.Show(sqlException.Message);
                    } 
                }
                else
                {
                    MessageBox.Show("Please input distributor id!");
                }
            }catch(FormatException ex) 
            {
                MessageBox.Show(ex.Message);
            }
            
        }

        private void RemoveButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("DELETE FROM DrinkTypes WHERE DTypeID = @DtypeID", dbConnection);
            if (cIdBox.Text.Length != 0)
            {
                int DTypeid = Int32.Parse(cIdBox.Text);
                command.Parameters.Add("@DtypeID", SqlDbType.Int);
                command.Parameters["@DtypeID"].Value = DTypeid;
                try
                {
                    daCard.DeleteCommand = command;
                    int numberOfDeleteTypes = daCard.DeleteCommand.ExecuteNonQuery();
                    if (numberOfDeleteTypes == 0)
                    {
                        MessageBox.Show("There is no drink type with the given id!");
                    }
                    else
                    {
                        ReloadDrinkTypesTableView();
                    }
                }
                catch (SqlException sqlException)
                {
                    MessageBox.Show(sqlException.ToString());
                }
            }
            else
                MessageBox.Show("Please provide a drinkType id!");
        
        }

        private void UpdateButton_Click(object sender, EventArgs e)
        {
            SqlCommand command = new SqlCommand("UPDATE DrinkTypes " +
                "SET DIStrid = @DIStrID, Type=@type "+
                "WHERE DTypeid = @DtypeID", dbConnection);

            int DTypedID = Int32.Parse(cIdBox.Text);
            int DIStrID = Int32.Parse(tracerBox.Text);;
            command.Parameters.Add("@DtypeID", SqlDbType.Int);
            command.Parameters["@DtypeID"].Value = DTypedID;
            command.Parameters.Add("@DIStrID", SqlDbType.Int);
            command.Parameters["@DIStrID"].Value = DIStrID;
            command.Parameters.Add("@type", SqlDbType.VarChar, 50);
            command.Parameters["@type"].Value = pIdBox.Text;
  
            try
            {
                daCard.UpdateCommand = command;
                int numberOfUpdatedSingers = daCard.UpdateCommand.ExecuteNonQuery();
                if (numberOfUpdatedSingers != 0)
                {
                    ReloadDrinkTypesTableView();
                }
                else
                {
                    MessageBox.Show("There is no drink type with the given id!");
                }
            }
            catch (SqlException sqlException)
            {
                if (sqlException.Number == 2627)
                    MessageBox.Show("The drink type id must be unique!");
                else if (sqlException.Number == 547)
                    MessageBox.Show("There's no distributor with the given id!");
                else
                    MessageBox.Show(sqlException.Message);
            }
        }

        private void TypeBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void DistributorsView_SelectionChanged(object sender, EventArgs e)
        {
            cIdBox.Clear();
            pIdBox.Clear();
            tracerBox.Clear();

            if(dgvPlayers.SelectedRows.Count!=0)
            {
                DataGridViewRow selectedRow = dgvPlayers.SelectedRows[0];
                daCard.SelectCommand = new SqlCommand("Select * FROM DrinkTypes WHERE DIStrid=" + selectedRow.Cells[0].Value, dbConnection);
                ReloadDrinkTypesTableView();
            }
        }

        private void DrinkTypesView_SelectionChanged(Object sender, EventArgs e)
        {
            if(dgvCards.SelectedRows.Count!=0)
            {
                DataGridViewRow selectedRow= dgvCards.SelectedRows[0];
                cIdBox.Text = selectedRow.Cells[0].Value.ToString();
                pIdBox.Text = selectedRow.Cells[1].Value.ToString();
                tracerBox.Text = selectedRow.Cells[2].Value.ToString();
            }
        }

    }
}

