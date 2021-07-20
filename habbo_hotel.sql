-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 21-Jul-2021 às 01:25
-- Versão do servidor: 10.4.19-MariaDB
-- versão do PHP: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `habbo_hotel`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_clientes`
--

CREATE TABLE `tb_clientes` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(60) NOT NULL,
  `cpf` varchar(15) NOT NULL,
  `senha` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tb_clientes`
--

INSERT INTO `tb_clientes` (`id`, `name`, `email`, `cpf`, `senha`) VALUES
(14, 'Gabriel Cabral', 'gabrielcabral352@gmail.com', '501.232.018-29', '1234');

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_reservas`
--

CREATE TABLE `tb_reservas` (
  `id` int(11) NOT NULL,
  `cliente` int(11) NOT NULL,
  `data_ini` datetime NOT NULL,
  `data_end` datetime NOT NULL,
  `quarto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tb_reservas`
--

INSERT INTO `tb_reservas` (`id`, `cliente`, `data_ini`, `data_end`, `quarto`) VALUES
(1, 14, '0000-00-00 00:00:00', '0000-00-00 00:00:00', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_suites`
--

CREATE TABLE `tb_suites` (
  `id` int(11) NOT NULL,
  `identifica` varchar(30) NOT NULL,
  `sit` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tb_suites`
--

INSERT INTO `tb_suites` (`id`, `identifica`, `sit`) VALUES
(1, 'Quarto 1', 1),
(2, 'Quarto 2', 0),
(3, 'Quarto 3', 0),
(4, 'Quarto 4', 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `tb_clientes`
--
ALTER TABLE `tb_clientes`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `tb_reservas`
--
ALTER TABLE `tb_reservas`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `tb_suites`
--
ALTER TABLE `tb_suites`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tb_clientes`
--
ALTER TABLE `tb_clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de tabela `tb_reservas`
--
ALTER TABLE `tb_reservas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tb_suites`
--
ALTER TABLE `tb_suites`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
