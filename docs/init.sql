--
-- PostgreSQL database dump
--

-- Dumped from database version 10.3
-- Dumped by pg_dump version 12.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

--
-- Name: el_course_meta; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.el_course_meta (
    id integer NOT NULL,
    duration interval NOT NULL,
    max_students integer NOT NULL,
    start_date date NOT NULL,
    instructor_id integer NOT NULL,
    crs_id integer NOT NULL
);


--
-- Name: el_course_meta_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.el_course_meta_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: el_course_meta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.el_course_meta_id_seq OWNED BY public.el_course_meta.id;


--
-- Name: el_course_meta id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.el_course_meta ALTER COLUMN id SET DEFAULT nextval('public.el_course_meta_id_seq'::regclass);


--
-- Data for Name: el_course_meta; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.el_course_meta (id, duration, max_students, start_date, instructor_id, crs_id) FROM stdin;
\.


--
-- Name: el_course_meta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.el_course_meta_id_seq', 1, false);


--
-- Name: el_course_meta el_course_meta_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.el_course_meta
    ADD CONSTRAINT el_course_meta_pkey PRIMARY KEY (id);


--
-- Name: el_course_meta_crs_id_a77d43df; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX el_course_meta_crs_id_a77d43df ON public.el_course_meta USING btree (crs_id);


--
-- Name: el_course_meta_instructor_id_21d8d876; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX el_course_meta_instructor_id_21d8d876 ON public.el_course_meta USING btree (instructor_id);


--
-- Name: el_course_meta el_course_meta_crs_id_a77d43df_fk_el_course_basemodel_ptr_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.el_course_meta
    ADD CONSTRAINT el_course_meta_crs_id_a77d43df_fk_el_course_basemodel_ptr_id FOREIGN KEY (crs_id) REFERENCES public.el_course(basemodel_ptr_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: el_course_meta el_course_meta_instructor_id_21d8d876_fk_authtools_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.el_course_meta
    ADD CONSTRAINT el_course_meta_instructor_id_21d8d876_fk_authtools_user_id FOREIGN KEY (instructor_id) REFERENCES public.authtools_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

