using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
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
        private SqlDataAdapter daParent, daChild;
        private DataSet tableData;
        private DataRelation drParentChild;
        BindingSource bsParent, bsChild;
        private List<TextBox> textBoxes;

        public Form1()
        {
            textBoxes = new List<TextBox>();
            InitializeComponent();
            loadTextboxes();
        }

        private void ReloadDrinkTypesTableView()
        {   
            string childTable = ConfigurationManager.AppSettings["ChildTableName"];
            if (tableData.Tables[childTable]!=null)
                tableData.Tables[childTable].Clear();

            daChild.Fill(tableData, childTable);
            dgChild.DataSource = bsChild;
            
        }

        private void loadTextboxes()
        {
            try
            {
                // We create a list of strings which contains the columnNames
                // The columnNames are splitted by ','
                List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ColumnNames"].Split(','));

                // We fix 2 points for X and Y, in order to place the textBoxes
                int pointX = 170;
                int pointY = 410;

                ////We take the number of columns and we clear the panel, before placing the new textBoxes
                //int numberOfColumns = Convert.ToInt32(ConfigurationManager.AppSettings["NumberOfColumns"]);
                panel.Controls.Clear();

                foreach (string columnName in ColumnNames)
                {
                    // We create a new textbox
                    TextBox a = new TextBox();
                    textBoxes.Add(a);
                    a.Text = columnName;
                    a.Name = columnName;
                    a.Location = new Point(pointX, pointY);
                    a.Visible = true;
                    a.Parent = panel;
                    panel.Show();
                    pointY -= 30;
                }
            }
            catch (Exception e)
            {
                MessageBox.Show(e.ToString());
            }

        }


        private void clearTextBoxes()
        {
            foreach (TextBox tb in textBoxes)
            {
                tb.Clear();
            }
        }

        private void ConnectButton_Click_1(object sender, EventArgs e)
        {
            dbConnection = new SqlConnection("Data Source=PAULIE\\SQLEXPRESS;Initial Catalog=BarManager;Integrated Security=True");
            dbConnection.Open();

            string selectParent = ConfigurationManager.AppSettings["ParentSelectQuery"];
            string parentTable = ConfigurationManager.AppSettings["ParentTableName"];

            daParent = new SqlDataAdapter(selectParent, dbConnection);
            tableData = new DataSet();
            daParent.Fill(tableData, parentTable);
            dgParent.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            string selectChild= ConfigurationManager.AppSettings["ChildSelectQuery"];
            string childTable = ConfigurationManager.AppSettings["ChildTableName"];

            daChild = new SqlDataAdapter(selectChild, dbConnection);
            daChild.Fill(tableData, childTable);
            dgChild.SelectionMode = DataGridViewSelectionMode.FullRowSelect;

            string fk = ConfigurationManager.AppSettings["ChildForeignKey"];
            DataColumn managerIdParent = tableData.Tables[parentTable].Columns[fk];
            DataColumn managerIdChild = tableData.Tables[childTable].Columns[fk];

            string foreingKey = ConfigurationManager.AppSettings["ForeingKey"];
            drParentChild = new DataRelation(foreingKey, managerIdParent, managerIdChild);
            tableData.Relations.Add(drParentChild);

            bsParent = new BindingSource();
            bsParent.DataSource = tableData;
            bsParent.DataMember = parentTable;

            bsChild = new BindingSource();
            bsChild.DataSource = bsParent;
            bsChild.DataMember = foreingKey;
            dgParent.DataSource = bsParent;

        }

        private void DistributorsView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void AddButton_Click(object sender, EventArgs e)
        {
            try
            {
                // We take the insert command
                string insertCommand = ConfigurationSettings.AppSettings["InsertQuery"];

                // We create the insert command
                this.daChild.InsertCommand = new SqlCommand(insertCommand, this.dbConnection);

                // We take the childTable's name
                string childTableName = ConfigurationManager.AppSettings["ChildTableName"];

                // We create a list with the column names of the child table which are splited by ','

                List<string> columnNamesList = new List<string>(ConfigurationManager.AppSettings["ColumnNames"].Split(','));

                // We go throguh all these columnNames
                // And then we parse the list of textBoxes in order to find the one whose name is the same as the columnName 
                foreach (string columnName in columnNamesList)
                {
                    foreach (TextBox tb in this.textBoxes)
                    {
                        if (tb.Name == columnName)
                        {
                            // After we find it, we insert to the coresponding parameter, the text from the textBox 
                            this.daChild.InsertCommand.Parameters.AddWithValue("@" + columnName, tb.Text);
                        }
                    }
                }

                // We open the connection and execute the query
                //this.dbConnection.Open();
                this.daChild.InsertCommand.ExecuteNonQuery();

                MessageBox.Show("Inserted with succes!");

                // We update the child table
                this.tableData = new DataSet();
                this.daChild.Fill(this.tableData, childTableName);
                this.dgChild.DataSource = this.tableData.Tables[childTableName];

                this.clearTextBoxes();

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                this.dbConnection.Close();
            }

        }

        private void RemoveButton_Click(object sender, EventArgs e)
        {
            string childId = ConfigurationManager.AppSettings["ChildId"];

            SqlCommand command = new SqlCommand("DELETE FROM " + ConfigurationManager.AppSettings["ChildTableName"] +
                " WHERE " + childId + "= @" + childId, dbConnection);

            foreach(TextBox tb in textBoxes)
            {
                if(tb.Name==childId)
                {
                    if(tb.Text.Length !=0)
                    {
                        int id=Int32.Parse(tb.Text);
                        command.Parameters.Add("@" + childId, SqlDbType.Int);
                        command.Parameters["@"+childId].Value= id;

                        try
                        {
                            daChild.DeleteCommand = command;
                            int numberofdeleted = daChild.DeleteCommand.ExecuteNonQuery();
                            if(numberofdeleted > 0)
                            {
                                MessageBox.Show("Deleted successfully!");
                                ReloadDrinkTypesTableView();
                            }
                            else
                            {
                                MessageBox.Show("No record with given id found!");
                            } 
                        }
                        catch(SqlException ex)
                        {
                            MessageBox.Show(ex.ToString());
                        }
                    }
                    else
                    {
                        MessageBox.Show("Please input id");
                    }
                    break;
                }
            }
        
        }

        private void UpdateButton_Click(object sender, EventArgs e)
        {
            try
            {
                string updateCommand = ConfigurationManager.AppSettings["UpdateQuery"];

                this.daChild.UpdateCommand = new SqlCommand(updateCommand, this.dbConnection);

                string childTableName = ConfigurationManager.AppSettings["ChildTableName"];

                List<string> columnNames = new List<string>(ConfigurationManager.AppSettings["ColumnNames"].Split(','));

                foreach(string columnName in columnNames)
                {
                    foreach(TextBox tb in textBoxes)
                    {
                        if(tb.Name==columnName)
                        {
                            this.daChild.UpdateCommand.Parameters.AddWithValue("@" + columnName, tb.Text);
                        }
                    }
                }

                this.daChild.UpdateCommand.ExecuteNonQuery();
                MessageBox.Show("Updated with success");

                this.tableData = new DataSet();
                this.daChild.Fill(this.tableData, childTableName);
                this.dgChild.DataSource = this.tableData.Tables[childTableName];

                foreach(TextBox tb in textBoxes)
                {
                    tb.Clear();
                }
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            
        }

        private void DTypeIdBox_TextChanged(object sender, EventArgs e)
        {

        }

        private void DistributorsView_SelectionChanged(object sender, EventArgs e)
        {
            if(dgParent.SelectedRows.Count!=0)
            {
                DataGridViewRow selectedRow = dgParent.SelectedRows[0];
                daChild.SelectCommand = new SqlCommand("Select * FROM " +
                    ConfigurationManager.AppSettings["ChildTableName"]+
                    " WHERE " + ConfigurationManager.AppSettings["ParentId"]+ "=" + selectedRow.Cells[0].Value, dbConnection);
                ReloadDrinkTypesTableView();
            }
        }

        private void DrinkTypesView_SelectionChanged(Object sender, EventArgs e)
        {
            if(dgChild.SelectedRows.Count!=0)
            {
                DataGridViewRow selectedRow= dgChild.SelectedRows[0];
            }
        }

    }
}

