# -*- coding: utf-8 -*-
# python

"""
The module supplies a dictionnary to store sql queries
"""

sql_dict = {
	"tro.datedrop_before" :
		[1, "ALTER TABLE tro DROP COLUMN IF EXISTS annee_tra2, DROP COLUMN IF EXISTS annee_cat2; \
		ALTER TABLE deb DROP COLUMN IF EXISTS annee_tra2;"],
	"deb.datedrop_before" :
		[2, "ALTER TABLE deb DROP COLUMN IF EXISTS annee_tra2;"],
	"tro.dateformat" :
		[3, "ALTER TABLE tro ADD COLUMN annee_tra2 date, ADD COLUMN annee_cat2 date; \
		ALTER TABLE deb ADD COLUMN annee_tra2 date;\
		UPDATE tro SET annee_tra2 = \
		(CASE WHEN annee_trav > 0 \
		THEN to_date(to_char(annee_trav, '99999999'), 'YYYYMMDD') \
		END);\
		UPDATE tro SET annee_cat2 = \
		(CASE WHEN annee_cat > 0 \
		THEN to_date(to_char(annee_cat, '99999999'), 'YYYYMMDD') \
		END);\
		UPDATE deb SET annee_tra2 = \
		(CASE WHEN annee_trav > 0 \
		THEN to_date(to_char(annee_trav, '99999999'), 'YYYYMMDD') \
		END);"],
	"deb.dateformat" :
		[4, "ALTER TABLE deb DROP COLUMN IF EXISTS annee_tra2; \
		ALTER TABLE deb ADD COLUMN annee_tra2 date;\
		UPDATE deb SET annee_tra2 = \
		(CASE WHEN annee_trav > 0 \
		THEN to_date(to_char(annee_trav, '99999999'), 'YYYYMMDD') \
		END);"],
	"tro.type_tro" :
		[5, "UPDATE tro SET type_tro=\
		(CASE \
		WHEN cat_projet='1CB' THEN 'DFCI' \
		WHEN cat_projet='2CB' THEN 'DFCI' \
		WHEN cat_projet='1CG' THEN 'DFCI' \
		WHEN cat_projet='2CG' THEN 'DFCI' \
		END);"],
	"tro.type_imp" :
		[6, "UPDATE tro SET type_imp=\
		(CASE \
		WHEN EXTRACT (YEAR FROM age(now(), tro.annee_tra2)) > 5 \
		OR tro.annee_tra2 IS NULL \
		THEN 'GABARIT' \
		END); \
		UPDATE tro SET type_imp=\
		(CASE \
		WHEN EXTRACT (YEAR FROM age(now(), deb.annee_tra2)) > 5 \
		OR deb.annee_tra2 IS NULL\
		THEN 'GABARIT' \
		END)\
		FROM deb \
		WHERE tro.zid_tro = deb.zid_tro;"],
	"tro.croise" :
		[7, "UPDATE tro SET croise='SANS'; \
		UPDATE tro SET croise=\
		(CASE \
		WHEN larg_pf = 6 AND EXTRACT (YEAR FROM age(now(), tro.annee_tra2)) <= 5 \
		AND EXTRACT (YEAR FROM age(now(), deb.annee_tra2)) <= 5 \
		THEN 'GENERALISEE' \
		WHEN larg_pf = 6 AND EXTRACT (YEAR FROM age(now(), tro.annee_tra2)) > 5 \
		AND EXTRACT (YEAR FROM age(now(), deb.annee_tra2)) > 5 \
		THEN 'PONCTUELLE' \
		WHEN larg_pf = 4 AND EXTRACT (YEAR FROM age(now(), tro.annee_tra2)) <= 5 \
		AND EXTRACT (YEAR FROM age(now(), deb.annee_tra2)) <= 5 \
		THEN 'PONCTUELLE' \
		WHEN larg_pf = 4 AND EXTRACT (YEAR FROM age(now(), tro.annee_tra2)) > 5 \
		AND EXTRACT (YEAR FROM age(now(), deb.annee_tra2)) > 5 \
		THEN 'SANS' \
		ELSE 'SANS' \
		END)\
		FROM deb \
		WHERE tro.zid_tro = deb.zid_tro;"],
	"tro.categorie" :
		[8, "UPDATE tro SET categorie=\
		(CASE \
		WHEN annee_cat2 IS NOT NULL AND type_imp IS NULL AND impasse='SANS' AND croise ='GENERALISEE' AND retourn='OUI' THEN '1C' \
		WHEN annee_cat2 IS NOT NULL AND type_imp IS NULL AND croise='PONCTUELLE' AND retourn='OUI' THEN '2C' \
		WHEN circ_gif='IMP' THEN 'HC' \
		ELSE 'HC' \
		END);"],
	"tro.long_m" :
		[9, "UPDATE tro SET long_m=round(ST_Length(geom));"],
	"tro.presta" :
		[10, "UPDATE tro SET presta=\
		(CASE \
		WHEN annee_tra2 IS NOT NULL THEN 'AUTRE'\
		END);"],
	"tro.foncier" :
		[11, "UPDATE tro SET foncier=\
		(CASE \
		WHEN date_serv IS NOT NULL AND date_serv != 0 THEN 'SE' \
		END);"],
	"deb.mois_trav" :
		[12, "UPDATE deb SET mois_trav=\
		EXTRACT (MONTH FROM annee_tra2);"],
	"deb.edition" :
		[13, "UPDATE deb SET edition=\
		EXTRACT (YEAR FROM annee_tra2) + 3;"],
	"deb.surf_ha" :
		[14, "UPDATE deb SET surf_ha =\
		subquery.result \
		FROM (SELECT deb.zid_deb as deb_key, round((deb.larg_deb * tro.long_m) / 10000.0, 1) as result \
		FROM tro, deb \
		WHERE tro.zid_tro = deb.zid_tro) as subquery \
		WHERE deb.zid_deb = subquery.deb_key;"],
	"deb.type_trav" :
		[15, "UPDATE deb SET type_trav =\
		(CASE \
		WHEN annee_tra2 IS NULL THEN 'MODIFIER' \
		WHEN annee_tra2 IS NOT NULL THEN 'ENTRETENIR' \
		END);"],
	"tro.datedrop_after" :
		[16, "ALTER TABLE tro DROP COLUMN IF EXISTS annee_tra2, DROP COLUMN IF EXISTS annee_cat2; \
		ALTER TABLE deb DROP COLUMN IF EXISTS annee_tra2;"],
	"deb.datedrop_after" :
		[17, "ALTER TABLE deb DROP COLUMN IF EXISTS annee_tra2;"]
}