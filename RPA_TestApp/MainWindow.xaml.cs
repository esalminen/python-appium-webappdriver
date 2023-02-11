using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace RPA_TestApp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void btnHelloText_Click(object sender, RoutedEventArgs e)
        {
            tbBtnText.Text = "Hello";
        }

        private void btnHowText_Click(object sender, RoutedEventArgs e)
        {
            tbBtnText.Text = "How are you?";
        }

        private void btnSeeText_Click(object sender, RoutedEventArgs e)
        {
            tbBtnText.Text = "See you later!";
        }

        private void btnGoodbyeText_Click(object sender, RoutedEventArgs e)
        {
            tbBtnText.Text = "Goodbye";
        }
    }
}
