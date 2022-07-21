-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Czas generowania: 21 Lip 2022, 16:18
-- Wersja serwera: 8.0.26
-- Wersja PHP: 8.0.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `s407396`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `opinion`
--

CREATE TABLE `opinion` (
  `id` int NOT NULL,
  `user_name` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `message` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Zrzut danych tabeli `opinion`
--

INSERT INTO `opinion` (`id`, `user_name`, `message`, `created_at`) VALUES
(43, 'Maciek', 'SUPER PIZZA', '2022-07-20 14:06:33'),
(44, 'Tomasz05', 'Polecam, najlepsza pizza w miescie, a nawet i w powiecie', '2022-07-20 14:13:43'),
(45, 'user5454', 'slabe, jadlem lepsze, malo kreatywne smaki, a kucharz beznadziejny', '2022-07-20 14:14:14'),
(46, 'TOMSon', 'Wyśmienita restauracja włoska. Przepyszne pizza. Ciasto rewelacja cieniutkie, składniki włoskie pierwsza klasa. Restauracja klimatyczna z miłą obsługą. Bardzo serdecznie polecam mimo że czasem na stolik musimy poczekać.', '2022-07-20 14:15:10'),
(47, 'Martyna96', 'Kameralne miejsce z bardzo dobrą pizzą. Mnie urzekł jednak krem z pomidorów - lepszego nie jadłam. Próbowałam również lasagne- ogromna porcja, całkiem smaczna natomiast dostałam leciutko przypaloną na wierzchu - mimo wszystko nie zepsuło to smaku i dobrego wrażenia.', '2022-07-20 14:15:32'),
(48, 'wojtaz', 'Pierwsza wizyta zakończona zgodnie z planem, pyszną włoską pizzą, charakteryzująca się świetnym cienkim ciastem, niebiańskimi dodatkami i najlepszą oliwą. Będziemy odwiedzać często i gorąco polecam to miejsce!', '2022-07-20 14:16:24'),
(49, 'KONESER PICC', 'Bardzo dobra włoska pizza, do tego super obsługa i bardzo ładny wystrój lokalu.\r\nJednak po ostatniej wizycie jestem niezadowolona ponieważ z menu zniknela moja ulubiona pizza kebab', '2022-07-20 14:18:02'),
(50, 'BIG', 'rzal pe el slaboo', '2022-07-20 14:18:26'),
(51, 'Dowolny nick', 'bardzo dobra pizza', '2022-07-21 16:15:12');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `order`
--

CREATE TABLE `order` (
  `id` int NOT NULL,
  `first_name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_number` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `street_and_house_number` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordered_pizzas` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `order_value` float DEFAULT NULL,
  `is_paid` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Zrzut danych tabeli `order`
--

INSERT INTO `order` (`id`, `first_name`, `last_name`, `phone_number`, `email`, `city`, `street_and_house_number`, `ordered_pizzas`, `order_value`, `is_paid`) VALUES
(73, 'g', '7', '222222222', 'po@d', 'Kraków', 'Rusznikarska', '{\"name\": \"Margherita\", \"rozmiar\": \"50.0\" \"ingredients\": \"sos, ser, szynka, bekon\" }\n', 52.9, 1),
(74, 'Jan', 'Kowalski', '123123123', 'arturstrozik@student.agh.edu.pl', 'Kraków', 'Czarnowiejska 45', '{\"name\": \"Margherita\", \"rozmiar\": \"40.0\" \"ingredients\": \"sos, ser, oliwki, kukurydza\" }\n{\"name\": \"Capri\", \"rozmiar\": \"30.0\" \"ingredients\": \"sos, ser, szynka, pieczarki, papryka, ananas\" }\n', 78.3, 1);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pizza`
--

CREATE TABLE `pizza` (
  `id` int NOT NULL,
  `pizza_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_sauce` tinyint(1) DEFAULT NULL,
  `is_cheese` tinyint(1) DEFAULT NULL,
  `is_ham` tinyint(1) DEFAULT NULL,
  `is_champignons` tinyint(1) DEFAULT NULL,
  `is_pepper` tinyint(1) DEFAULT NULL,
  `is_olives` tinyint(1) DEFAULT NULL,
  `is_bacon` tinyint(1) DEFAULT NULL,
  `is_corn` tinyint(1) DEFAULT NULL,
  `is_tuna` tinyint(1) DEFAULT NULL,
  `is_pineapple` tinyint(1) DEFAULT NULL,
  `price_30` float DEFAULT NULL,
  `price_40` float DEFAULT NULL,
  `price_50` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Zrzut danych tabeli `pizza`
--

INSERT INTO `pizza` (`id`, `pizza_name`, `is_sauce`, `is_cheese`, `is_ham`, `is_champignons`, `is_pepper`, `is_olives`, `is_bacon`, `is_corn`, `is_tuna`, `is_pineapple`, `price_30`, `price_40`, `price_50`) VALUES
(1, 'Margherita', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 25.9, 34.9, 42.9),
(2, 'Funghi', 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 27.9, 36.9, 44.9),
(3, 'Diego', 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 30.9, 41.9, 48.9),
(4, 'Capri', 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 31.9, 43.9, 49.9),
(5, 'Amore', 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 32.9, 44.9, 50.9),
(6, 'Siciliana', 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 33.9, 45.9, 51.9);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pizza_customize`
--

CREATE TABLE `pizza_customize` (
  `id` int NOT NULL,
  `pizza_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_sauce` tinyint(1) DEFAULT NULL,
  `is_cheese` tinyint(1) DEFAULT NULL,
  `is_ham` tinyint(1) DEFAULT NULL,
  `is_champignons` tinyint(1) DEFAULT NULL,
  `is_pepper` tinyint(1) DEFAULT NULL,
  `is_olives` tinyint(1) DEFAULT NULL,
  `is_bacon` tinyint(1) DEFAULT NULL,
  `is_corn` tinyint(1) DEFAULT NULL,
  `is_tuna` tinyint(1) DEFAULT NULL,
  `is_pineapple` tinyint(1) DEFAULT NULL,
  `size` float DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `opinion`
--
ALTER TABLE `opinion`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `pizza`
--
ALTER TABLE `pizza`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `pizza_customize`
--
ALTER TABLE `pizza_customize`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `opinion`
--
ALTER TABLE `opinion`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT dla tabeli `order`
--
ALTER TABLE `order`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;

--
-- AUTO_INCREMENT dla tabeli `pizza`
--
ALTER TABLE `pizza`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT dla tabeli `pizza_customize`
--
ALTER TABLE `pizza_customize`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
