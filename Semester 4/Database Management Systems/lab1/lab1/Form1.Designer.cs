namespace lab1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dgvPlayers = new System.Windows.Forms.DataGridView();
            this.dgvCards = new System.Windows.Forms.DataGridView();
            this.cIdBox = new System.Windows.Forms.TextBox();
            this.pIdBox = new System.Windows.Forms.TextBox();
            this.tracerBox = new System.Windows.Forms.TextBox();
            this.cIdLabel = new System.Windows.Forms.Label();
            this.pIdLabel = new System.Windows.Forms.Label();
            this.tracerLabel = new System.Windows.Forms.Label();
            this.AddButton = new System.Windows.Forms.Button();
            this.RemoveButton = new System.Windows.Forms.Button();
            this.UpdateButton = new System.Windows.Forms.Button();
            this.ConnectButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dgvPlayers)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvCards)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvPlayers
            // 
            this.dgvPlayers.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvPlayers.Location = new System.Drawing.Point(68, 62);
            this.dgvPlayers.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.dgvPlayers.Name = "dgvPlayers";
            this.dgvPlayers.RowHeadersWidth = 62;
            this.dgvPlayers.Size = new System.Drawing.Size(378, 242);
            this.dgvPlayers.TabIndex = 0;
            this.dgvPlayers.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.DistributorsView_CellContentClick);
            this.dgvPlayers.SelectionChanged += new System.EventHandler(this.DistributorsView_SelectionChanged);
            // 
            // dgvCards
            // 
            this.dgvCards.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvCards.Location = new System.Drawing.Point(746, 72);
            this.dgvCards.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.dgvCards.Name = "dgvCards";
            this.dgvCards.RowHeadersWidth = 62;
            this.dgvCards.Size = new System.Drawing.Size(358, 231);
            this.dgvCards.TabIndex = 1;
            this.dgvCards.SelectionChanged += new System.EventHandler(this.DrinkTypesView_SelectionChanged);
            // 
            // cIdBox
            // 
            this.cIdBox.Location = new System.Drawing.Point(180, 389);
            this.cIdBox.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.cIdBox.Name = "cIdBox";
            this.cIdBox.Size = new System.Drawing.Size(148, 26);
            this.cIdBox.TabIndex = 2;
            // 
            // pIdBox
            // 
            this.pIdBox.Location = new System.Drawing.Point(180, 452);
            this.pIdBox.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.pIdBox.Name = "pIdBox";
            this.pIdBox.Size = new System.Drawing.Size(148, 26);
            this.pIdBox.TabIndex = 3;
            this.pIdBox.TextChanged += new System.EventHandler(this.TypeBox_TextChanged);
            // 
            // tracerBox
            // 
            this.tracerBox.Location = new System.Drawing.Point(180, 520);
            this.tracerBox.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.tracerBox.Name = "tracerBox";
            this.tracerBox.Size = new System.Drawing.Size(148, 26);
            this.tracerBox.TabIndex = 4;
            // 
            // cIdLabel
            // 
            this.cIdLabel.AutoSize = true;
            this.cIdLabel.Location = new System.Drawing.Point(68, 398);
            this.cIdLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.cIdLabel.Name = "cIdLabel";
            this.cIdLabel.Size = new System.Drawing.Size(70, 20);
            this.cIdLabel.TabIndex = 5;
            this.cIdLabel.Text = "cIdLabel";
            // 
            // pIdLabel
            // 
            this.pIdLabel.AutoSize = true;
            this.pIdLabel.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.pIdLabel.Location = new System.Drawing.Point(72, 462);
            this.pIdLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.pIdLabel.Name = "pIdLabel";
            this.pIdLabel.Size = new System.Drawing.Size(71, 20);
            this.pIdLabel.TabIndex = 6;
            this.pIdLabel.Text = "pIdLabel";
            this.pIdLabel.Click += new System.EventHandler(this.label2_Click);
            // 
            // tracerLabel
            // 
            this.tracerLabel.AutoSize = true;
            this.tracerLabel.Location = new System.Drawing.Point(68, 529);
            this.tracerLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.tracerLabel.Name = "tracerLabel";
            this.tracerLabel.Size = new System.Drawing.Size(89, 20);
            this.tracerLabel.TabIndex = 7;
            this.tracerLabel.Text = "tracerLabel";
            // 
            // AddButton
            // 
            this.AddButton.Location = new System.Drawing.Point(630, 389);
            this.AddButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.AddButton.Name = "AddButton";
            this.AddButton.Size = new System.Drawing.Size(112, 35);
            this.AddButton.TabIndex = 8;
            this.AddButton.Text = "Add";
            this.AddButton.UseVisualStyleBackColor = true;
            this.AddButton.Click += new System.EventHandler(this.AddButton_Click);
            // 
            // RemoveButton
            // 
            this.RemoveButton.Location = new System.Drawing.Point(630, 448);
            this.RemoveButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.RemoveButton.Name = "RemoveButton";
            this.RemoveButton.Size = new System.Drawing.Size(112, 35);
            this.RemoveButton.TabIndex = 9;
            this.RemoveButton.Text = "Remove";
            this.RemoveButton.UseVisualStyleBackColor = true;
            this.RemoveButton.Click += new System.EventHandler(this.RemoveButton_Click);
            // 
            // UpdateButton
            // 
            this.UpdateButton.Location = new System.Drawing.Point(628, 520);
            this.UpdateButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.UpdateButton.Name = "UpdateButton";
            this.UpdateButton.Size = new System.Drawing.Size(112, 35);
            this.UpdateButton.TabIndex = 10;
            this.UpdateButton.Text = "Update";
            this.UpdateButton.UseVisualStyleBackColor = true;
            this.UpdateButton.Click += new System.EventHandler(this.UpdateButton_Click);
            // 
            // ConnectButton
            // 
            this.ConnectButton.Location = new System.Drawing.Point(992, 448);
            this.ConnectButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.ConnectButton.Name = "ConnectButton";
            this.ConnectButton.Size = new System.Drawing.Size(112, 35);
            this.ConnectButton.TabIndex = 11;
            this.ConnectButton.Text = "Connect";
            this.ConnectButton.UseVisualStyleBackColor = true;
            this.ConnectButton.Click += new System.EventHandler(this.ConnectButton_Click_1);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.ClientSize = new System.Drawing.Size(1200, 692);
            this.Controls.Add(this.ConnectButton);
            this.Controls.Add(this.UpdateButton);
            this.Controls.Add(this.RemoveButton);
            this.Controls.Add(this.AddButton);
            this.Controls.Add(this.tracerLabel);
            this.Controls.Add(this.pIdLabel);
            this.Controls.Add(this.cIdLabel);
            this.Controls.Add(this.tracerBox);
            this.Controls.Add(this.pIdBox);
            this.Controls.Add(this.cIdBox);
            this.Controls.Add(this.dgvCards);
            this.Controls.Add(this.dgvPlayers);
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.dgvPlayers)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dgvCards)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvPlayers;
        private System.Windows.Forms.DataGridView dgvCards;
        private System.Windows.Forms.TextBox cIdBox;
        private System.Windows.Forms.TextBox pIdBox;
        private System.Windows.Forms.TextBox tracerBox;
        private System.Windows.Forms.Label cIdLabel;
        private System.Windows.Forms.Label pIdLabel;
        private System.Windows.Forms.Label tracerLabel;
        private System.Windows.Forms.Button AddButton;
        private System.Windows.Forms.Button RemoveButton;
        private System.Windows.Forms.Button UpdateButton;
        private System.Windows.Forms.Button ConnectButton;


        
    }
}

